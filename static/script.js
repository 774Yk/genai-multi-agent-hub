const agents = {
  support: { title: 'خدمة العملاء', welcome: 'ابدأ مع وكيل خدمة العملاء', hint: 'أرسل شكوى أو استفساراً، وسيعود الوكيل بتحليل منظم ورد مقترح.' },
  marketing: { title: 'التسويق', welcome: 'ابدأ مع وكيل التسويق', hint: 'ألصق مقالاً أو فكرة، وسيحوّلها الوكيل إلى محتوى مناسب للقنوات المختلفة.' },
  tutor: { title: 'معلم البرمجة', welcome: 'ابدأ مع معلم البرمجة', hint: 'أرسل لغة البرمجة والكود ورسالة الخطأ، وستحصل على تلميحات تدريجية.' }
};
let selectedAgent = 'support';
const messages = document.querySelector('#messages');
const input = document.querySelector('#messageInput');
const form = document.querySelector('#chatForm');
const sendButton = document.querySelector('#sendButton');
const timing = document.querySelector('#timing');

function escapeHtml(value) {
  return String(value ?? '').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[ch]));
}
function addUserMessage(text) {
  messages.querySelector('.welcome')?.remove();
  messages.insertAdjacentHTML('beforeend', `<div class="bubble user"><div class="bubble-label">أنت</div>${escapeHtml(text)}</div>`);
}
function addResult(data) {
  const labels = {summary:'الملخص',category:'الفئة',sentiment:'المشاعر',response:'الرد المقترح',next_step:'الخطوة التالية',hook:'العنوان الجاذب',twitter_post:'منشور X/Twitter',linkedin_post:'منشور LinkedIn',call_to_action:'الدعوة إلى الإجراء',language:'اللغة',error_analysis:'تحليل الخطأ',hint:'التلميح',concept:'المفهوم',next_question:'السؤال التالي'};
  const fields = Object.entries(data).filter(([key]) => !['agent','duration_seconds'].includes(key));
  const markup = fields.map(([key, value]) => `<div class="result-field ${['response','linkedin_post','hint','error_analysis'].includes(key) ? 'full' : ''}"><b>${labels[key] || key}</b><span>${escapeHtml(value)}</span></div>`).join('');
  messages.insertAdjacentHTML('beforeend', `<div class="bubble"><div class="bubble-label">نتيجة ${escapeHtml(agents[selectedAgent].title)}</div><div class="result-grid">${markup}</div></div>`);
  messages.scrollTop = messages.scrollHeight;
}

document.querySelectorAll('.agent-card').forEach(button => button.addEventListener('click', () => {
  selectedAgent = button.dataset.agent;
  document.querySelectorAll('.agent-card').forEach(item => item.classList.toggle('active', item === button));
  document.querySelector('#agentTitle').textContent = agents[selectedAgent].title;
  document.querySelector('#welcomeTitle').textContent = agents[selectedAgent].welcome;
  document.querySelector('#welcomeText').textContent = agents[selectedAgent].hint;
  timing.textContent = '';
}));

form.addEventListener('submit', async event => {
  event.preventDefault();
  const text = input.value.trim();
  if (!text || sendButton.disabled) return;
  addUserMessage(text);
  input.value = '';
  sendButton.disabled = true;
  sendButton.textContent = 'جاري التشغيل...';
  timing.textContent = '';
  try {
    const response = await fetch('/generate', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({agent: selectedAgent, message: text}) });
    const data = await response.json();
    if (!response.ok) throw new Error(data.details || data.error || 'تعذر تشغيل الوكيل');
    addResult(data);
    timing.textContent = `${data.duration_seconds} ثانية`;
  } catch (error) {
    messages.insertAdjacentHTML('beforeend', `<div class="bubble error"><div class="bubble-label">خطأ</div>${escapeHtml(error.message)}</div>`);
  } finally {
    sendButton.disabled = false;
    sendButton.innerHTML = 'تشغيل الوكيل <span>↗</span>';
    messages.scrollTop = messages.scrollHeight;
  }
});
input.addEventListener('keydown', event => { if (event.key === 'Enter' && !event.shiftKey) { event.preventDefault(); form.requestSubmit(); } });
