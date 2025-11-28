from datetime import datetime
from pathlib import Path
from app.inference import load_model, generate
from app.personalities import pick_two, system_prompt_for

def main():
    # Ensure model is ready
    load_model()

    # Pick two house voices and build a light system style
    a, b = pick_two()
    system = system_prompt_for(a, b)

    # Simple seed prompt
    user = "Write a compact terminal-core vignette about neon rain beading on old glass; keep it concrete."

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]

    out = generate(messages, max_new_tokens=128, temperature=0.7, top_p=0.95)

    # Save to outputs/
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = Path("outputs")
    out_dir.mkdir(parents=True, exist_ok=True)
    fname = out_dir / f"seed_{a.id}_{b.id}_{ts}.txt"
    fname.write_text(out, encoding="utf-8")

    print(f"wrote: {fname.as_posix()}")

if __name__ == "__main__":
    main()
