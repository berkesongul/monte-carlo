# 🎯 Monte Carlo Pi Estimation

A visual and interactive project that estimates the mathematical constant **π (Pi)** using the [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method) — one of the most elegant applications of randomness in computational mathematics.

Inspired by the [MarbleScience YouTube channel](https://www.youtube.com/@MarbleScience).

---

## 🧠 The Idea

Imagine dropping marbles randomly onto a square surface that has a circular bowl inscribed inside it. Some marbles land inside the circle, some land outside. The ratio of marbles inside the circle to the total gives us a way to estimate Pi:

$$\pi \approx 4 \times \frac{\text{Points Inside Circle}}{\text{Total Points}}$$

As more marbles are dropped, the estimate converges to the true value of Pi (**3.14159...**). This project brings that concept to life with real-time visuals and data.

---

## 📂 Project Structure

| File | Description |
|------|-------------|
| `monte-carlo-pi.py` | **2D Simulation** — Real-time Pygame animation with live stats and a Matplotlib convergence graph |
| `monte-carlo-pi-3d.py` | **3D Simulation** — Estimates Pi using a sphere inscribed in a cube, visualized with a 3D scatter plot |

---

## 🚀 Simulations

### 1. 2D Simulation (`monte-carlo-pi.py`)

An interactive Pygame window where marbles drop onto a square canvas one by one:

- 🔴 **Red** dots land **inside** the inscribed circle (hits)
- 🔵 **Blue** dots land **outside** the circle (misses)
- A **live info panel** shows total points, hits, current Pi estimate, and error margin
- On closing the window, a **Matplotlib line graph** displays how the Pi estimate converged over time

**Key parameters:**
```python
TOTAL_DROPS_TARGET = 1_000_000_000  # Total marbles to simulate
DROPS_PER_FRAME    = 20_000         # Marbles processed per frame (controls speed)
```

### 2. 3D Simulation (`monte-carlo-pi-3d.py`)

Extends the concept to three dimensions — random points are scattered inside a cube, and those falling within an inscribed **sphere** are counted:

$$\pi \approx 6 \times \frac{\text{Points Inside Sphere}}{\text{Total Points}}$$

A 3D scatter plot visualizes the result, with red points inside the sphere and blue points outside.

---

## 📦 Requirements

| Library | Purpose | Install |
|---------|---------|---------|
| **Pygame** | Real-time 2D rendering and animation | `pip install pygame` |
| **Matplotlib** | Convergence graph and 3D scatter plot | `pip install matplotlib` |
| **NumPy** | Vectorized math for the 3D simulation | `pip install numpy` |

> `random` and `math` are part of the Python standard library — no installation needed.

**Quick install:**
```bash
pip install pygame matplotlib numpy
```

---

## ▶️ Usage

```bash
# Run the 2D simulation (Pygame window + convergence graph)
python monte-carlo-pi.py

# Run the 3D simulation (3D scatter plot)
python monte-carlo-pi-3d.py
```

---

## 🔬 How It Works

### The Math Behind It

**2D (Circle in a Square):**
A circle of radius *r* has area `πr²`. The enclosing square has area `(2r)² = 4r²`. The ratio of areas is `π/4`, so:

```
π = 4 × (circle area / square area) ≈ 4 × (hits / total)
```

**3D (Sphere in a Cube):**
A sphere of radius *r* has volume `(4/3)πr³`. The enclosing cube has volume `(2r)³ = 8r³`. The ratio is `π/6`, so:

```
π = 6 × (sphere volume / cube volume) ≈ 6 × (hits / total)
```

### Convergence

The estimate improves as more points are sampled. With just a few hundred points, the estimate is rough; with millions, it approaches the true value of Pi with increasing precision. This is the **Law of Large Numbers** in action.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
