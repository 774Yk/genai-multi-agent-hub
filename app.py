import time

from flask import Flask, jsonify, render_template, request

from agents import marketing_agent, support_agent, tutor_agent

app = Flask(__name__)

AGENTS = {
    "support": support_agent.run,
    "marketing": marketing_agent.run,
    "tutor": tutor_agent.run,
}


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/health")
def health():
    return jsonify({"status": "ok", "agents": list(AGENTS)})


@app.post("/generate")
def generate():
    data = request.get_json(silent=True) or {}
    user_message = (data.get("message") or "").strip()
    agent_name = (data.get("agent") or "").strip().lower()

    if not user_message:
        return jsonify({"error": "Missing message"}), 400
    if agent_name not in AGENTS:
        return jsonify({"error": "Invalid agent selection", "available_agents": list(AGENTS)}), 400

    start_time = time.perf_counter()
    try:
        result = AGENTS[agent_name](user_message)
        result["agent"] = agent_name
        result["duration_seconds"] = round(time.perf_counter() - start_time, 2)
        return jsonify(result)
    except Exception as exc:
        app.logger.exception("Agent request failed")
        return jsonify({"error": "Agent request failed", "details": str(exc)}), 502


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
