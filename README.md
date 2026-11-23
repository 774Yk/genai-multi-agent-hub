# GenAI Multi-Agent Hub

مشروع تعليمي احترافي مبني باستخدام Flask وLangChain وOpenRouter، ويطبّق أفكار مختبر **Develop Generative AI Applications: Get Started** من Coursera في تطبيق واحد متعدد الوكلاء.

يتيح التطبيق للمستخدم التبديل بين ثلاثة وكلاء متخصصين، مع استخدام قوالب Prompts منفصلة ومخرجات JSON منظمة يمكن استهلاكها برمجيًا.

## الوكلاء

| الوكيل | الوظيفة | المخرجات المنظمة |
|---|---|---|
| Support | تحليل رسالة العميل وتصنيفها وتحليل المشاعر | `summary`, `category`, `sentiment`, `response`, `next_step` |
| Marketing | تحويل نص المصدر إلى محتوى تسويقي | `summary`, `hook`, `twitter_post`, `linkedin_post`, `call_to_action` |
| Tutor | تعليم تصحيح أخطاء البرمجة بالتلميحات | `language`, `error_analysis`, `hint`, `concept`, `next_question` |

## مطابقة أسلوب المختبر

يحافظ المشروع على الأفكار الأساسية الواردة في المختبر:

- تطبيق Flask لاستقبال الطلبات وعرض واجهة تفاعلية.
- ملف إعدادات مركزي لإدارة إعدادات النموذج.
- طبقة تكامل منفصلة مع النموذج عبر `ChatOpenAI`.
- استخدام `PromptTemplate` ودمج السلسلة باستخدام العامل `|`.
- استخدام `Pydantic` و`JsonOutputParser` لضمان مخرجات منظمة.
- فصل منطق كل وكيل في ملف مستقل، مع واجهة واحدة للتبديل بينها.
- الاتصال بواجهة OpenAI-compatible الخاصة بـ OpenRouter بدلًا من Watsonx.

## التشغيل

```bash
cd genai_multi_agent_hub
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENROUTER_API_KEY="your-key"
python app.py
```

افتح `http://127.0.0.1:5000` في المتصفح. لا تضع مفتاح API الحقيقي داخل Git أو ملفات المشروع. استخدم `.env.example` كمرجع فقط.

## اختبار API مباشرة

```bash
curl -X POST http://127.0.0.1:5000/generate \
  -H 'Content-Type: application/json' \
  -d '{"agent":"support","message":"تم خصم المبلغ مرتين من حسابي وأحتاج إلى المساعدة."}'
```

القيم المقبولة في الحقل `agent` هي: `support` و`marketing` و`tutor`.

## الاختبارات

```bash
pytest -q
```

## هيكل المشروع

```text
app.py
config.py
model.py
agents/
  support_agent.py
  marketing_agent.py
  tutor_agent.py
templates/index.html
static/styles.css
static/script.js
tests/test_app.py
requirements.txt
.env.example
.gitignore
LICENSE
```

## عن المطوّر

تم تطوير هذا المشروع بواسطة **Yassen** بهدف بناء مشروع عملي يوضح مهارات تطوير تطبيقات الذكاء الاصطناعي التوليدي، وهندسة الـ Prompts، وتصميم المخرجات المنظمة، وبناء واجهات Flask قابلة للتوسعة.

- البريد الإلكتروني: [yassenalhajere@gmail.com](mailto:yassenalhajere@gmail.com)
- LinkedIn: [linkedin.com/in/yassen-al-hajere-572427387](https://www.linkedin.com/in/yassen-al-hajere-572427387/)

## حقوق الملكية والترخيص

حقوق الطبع والنشر © 2026 **Yassen**. جميع الحقوق محفوظة للملفات الأصلية الخاصة بهذا المشروع.

هذا المشروع منشور بموجب [رخصة MIT](LICENSE). راجع ملف الترخيص لمعرفة شروط الاستخدام وإعادة التوزيع.

> ملاحظة: هذا المشروع تعليمي وتجريبي، ويتطلب مفتاح OpenRouter صالحًا لتشغيل الوكلاء عبر النموذج.
