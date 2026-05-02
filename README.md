# 🌸 Mandala Pattern Generator

> *A colorful, interactive generative art project built with Python's built-in `turtle` module — no pip installs needed!*

---

``` 
        ✦ ── ✦ ── ✦
      ╱               ╲
    ✦   🌸 MANDALA 🌸   ✦
      ╲               ╱
        ✦ ── ✦ ── ✦
```

---

## 📌 About

**Mandala Pattern Generator** ek Python project hai jo sirf `turtle` aur `colorsys` (dono built-in) use karke **5 beautiful generative art patterns** draw karta hai. Ek bhi library install nahi karni — bas run karo aur enjoy karo!

- 🎨 **HSV rainbow color cycling** — smooth gradient colors
- ⌨️ **Keyboard se pattern switch** — 1 se 5 key press karo
- ⚡ **Instant rendering** — `tracer(0)` se flicker-free drawing
- 🖤 **Black canvas** — maximum contrast aur drama

---

## 🖼️ Patterns

| Key | Pattern | Description |
|:---:|---------|-------------|
| `1` | 🌸 **Petal Mandala** | 36 overlapping rainbow arcs — classic mandala look |
| `2` | ⭐ **Star Burst** | 72 colorful spokes radiating from center |
| `3` | 🌀 **Spiral Mandala** | 8-sided polygon jo bahar ki taraf spiral karta hai |
| `4` | 🌹 **Rose Curve (Rhodonea)** | Mathematical rose — `r = cos(nθ)` — 2 layers |
| `5` | 🔵 **Layered Circles** | 12 concentric rings, har ring mein zyada circles |
| `Q` | ❌ **Quit** | Window band karo |

---

## 🚀 How to Run

Python built-in hai — kuch install nahi karna!

```bash
# Clone the repo
git clone https://github.com/yourusername/mandala-generator.git
cd mandala-generator

# Run karo
python mandala.py

# Ya python3 ke saath
python3 mandala.py
```

> ✅ **Requirements:** Python 3.x — Koi external library nahi!

---

## 📁 File Structure

```
mandala-generator/
│
└── mandala.py        # All 5 patterns + keyboard controls + menu
```

Yeh ek single-file project hai — sab kuch ek hi file mein! 🎯

---

## ⌨️ Controls

```
┌─────┬──────────────────────────────────────┐
│ Key │ Action                               │
├─────┼──────────────────────────────────────┤
│  1  │ 🌸 Draw Petal Mandala                │
│  2  │ ⭐ Draw Star Burst Mandala           │
│  3  │ 🌀 Draw Spiral Mandala              │
│  4  │ 🌹 Draw Rose Curve Mandala          │
│  5  │ 🔵 Draw Layered Circle Mandala      │
│  Q  │ ❌ Quit the program                  │
└─────┴──────────────────────────────────────┘
```

---

## ✨ Features

- ✅ 5 fully distinct generative art algorithms
- ✅ Smooth HSV rainbow colors (`colorsys` module)
- ✅ Instant pattern switching — restart nahi karna
- ✅ `tracer(0)` + `update()` — flicker-free rendering
- ✅ Auto-draws Pattern 1 on launch
- ✅ Black background for visual contrast
- ✅ Zero external dependencies

---

## 🧠 Concepts Covered

| Concept | Details |
|---------|---------|
| `turtle` graphics | Drawing, movement, color, speed |
| `colorsys` HSV | Smooth rainbow color generation |
| `math.sin / cos` | Polar coordinates for Rose curve |
| Keyboard events | `screen.onkey()` bindings |
| `screen.tracer(0)` | Fast, flicker-free animation |
| Lambda closures | Pattern switching handlers |
| Polar coordinates | Rose & circle calculations |

---

## 🔍 How It Works

```python
# HSV se rainbow colors
def set_color_hsv(hue, saturation=0.9, value=1.0):
    r, g, b = colorsys.hsv_to_rgb(hue % 1.0, saturation, value)
    t.pencolor(r, g, b)

# Rose curve math
r = scale * math.cos(petals * theta)
x = r * math.cos(theta)
y = r * math.sin(theta)

# Keyboard binding
screen.onkey(on_key(petal_mandala), "1")
```

---

## 🤝 Contributing

Pull requests welcome hai! Naya pattern add karna chahte ho? Fork karo aur PR bhejo! 🚀

1. Fork the project
2. Create your branch: `git checkout -b feature/new-pattern`
3. Commit: `git commit -m 'Add new pattern'`
4. Push: `git push origin feature/new-pattern`
5. Open a Pull Request

---

## 📄 License

MIT License — freely use, modify, and share! 🌍

---

<div align="center">

Made by piyushSoni using Python `turtle` · `colorsys` · `math`

⭐ **Star this repo agar pasand aaya!** ⭐

</div>
