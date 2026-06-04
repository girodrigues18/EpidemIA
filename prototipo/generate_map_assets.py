# -*- coding: utf-8 -*-
"""Gera SVGs de mapa + heatmap nítidos para o protótipo EpidemIA."""
from pathlib import Path

ASSETS = Path(r"e:\Gi_Pereira\GS - Space Connect\Pitch\assets")
ASSETS.mkdir(parents=True, exist_ok=True)

DASHBOARD_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="960" height="520">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1a2e3b"/>
      <stop offset="100%" stop-color="#0f1f18"/>
    </linearGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="#2d4a42" stroke-width="0.6" opacity="0.35"/>
    </pattern>
    <radialGradient id="g1" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.75"/>
      <stop offset="55%" stop-color="#10b981" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#10b981" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="g2" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#f59e0b" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="g3" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.9"/>
      <stop offset="45%" stop-color="#dc2626" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#dc2626" stop-opacity="0"/>
    </radialGradient>
    <filter id="sharp" x="-2%" y="-2%" width="104%" height="104%">
      <feComponentTransfer>
        <feFuncA type="discrete" tableValues="0 0.2 0.5 0.75 1"/>
      </feComponentTransfer>
    </filter>
  </defs>
  <rect width="960" height="520" fill="url(#sky)"/>
  <rect width="960" height="520" fill="url(#grid)"/>
  <!-- Blocos urbanos (satélite estilizado) -->
  <g fill="#1e3d32" opacity="0.85">
    <rect x="40" y="80" width="120" height="90" rx="2"/>
    <rect x="180" y="60" width="90" height="110" rx="2"/>
    <rect x="290" y="100" width="140" height="70" rx="2"/>
    <rect x="450" y="50" width="100" height="130" rx="2"/>
    <rect x="570" y="90" width="130" height="85" rx="2"/>
    <rect x="720" y="70" width="110" height="100" rx="2"/>
    <rect x="60" y="200" width="150" height="80" rx="2"/>
    <rect x="230" y="190" width="100" height="95" rx="2"/>
    <rect x="350" y="210" width="160" height="75" rx="2"/>
    <rect x="530" y="180" width="120" height="110" rx="2"/>
    <rect x="670" y="200" width="140" height="90" rx="2"/>
    <rect x="100" y="310" width="200" height="70" rx="2"/>
    <rect x="320" y="300" width="180" height="85" rx="2"/>
    <rect x="520" y="320" width="150" height="65" rx="2"/>
    <rect x="700" y="290" width="120" height="95" rx="2"/>
  </g>
  <g fill="#243d35" opacity="0.6">
    <rect x="130" y="140" width="60" height="40"/>
    <rect x="400" y="160" width="80" height="50"/>
    <rect x="600" y="240" width="70" height="45"/>
  </g>
  <!-- Camada heatmap (sem blur CSS — gradientes radiais nítidos) -->
  <ellipse cx="200" cy="180" rx="130" ry="100" fill="url(#g1)"/>
  <ellipse cx="420" cy="220" rx="110" ry="90" fill="url(#g2)"/>
  <ellipse cx="680" cy="160" rx="160" ry="120" fill="url(#g3)"/>
  <ellipse cx="320" cy="340" rx="100" ry="75" fill="url(#g1)" opacity="0.5"/>
  <ellipse cx="550" cy="280" rx="90" ry="70" fill="url(#g2)" opacity="0.45"/>
  <!-- Contorno área crítica 14-B -->
  <ellipse cx="700" cy="175" rx="95" ry="75" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="6 4" opacity="0.5"/>
  <text x="700" y="178" text-anchor="middle" fill="#fff" font-family="Segoe UI,sans-serif" font-size="11" font-weight="700" opacity="0.9">14-B</text>
</svg>
"""

AGENT_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 280" width="400" height="280">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e3a5f"/>
      <stop offset="50%" stop-color="#1a4d42"/>
      <stop offset="100%" stop-color="#0f4c45"/>
    </linearGradient>
    <radialGradient id="hot" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.95"/>
      <stop offset="40%" stop-color="#dc2626" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#dc2626" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="warm" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="400" height="280" fill="url(#bg)"/>
  <g fill="#1a3d35" opacity="0.5">
    <rect x="20" y="40" width="80" height="60"/><rect x="120" y="30" width="100" height="70"/>
    <rect x="240" y="50" width="90" height="55"/><rect x="50" y="130" width="120" height="50"/>
    <rect x="200" y="120" width="150" height="80"/>
  </g>
  <ellipse cx="240" cy="120" rx="120" ry="95" fill="url(#warm)" opacity="0.6"/>
  <ellipse cx="260" cy="110" rx="75" ry="60" fill="url(#hot)"/>
  <circle cx="260" cy="108" r="8" fill="#fff" stroke="#dc2626" stroke-width="3"/>
  <circle cx="260" cy="108" r="3" fill="#dc2626"/>
</svg>
"""

THUMB_SAT_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120" width="200" height="120">
  <rect width="200" height="120" fill="#1a3a2a"/>
  <ellipse cx="100" cy="60" rx="70" ry="45" fill="#ef4444" opacity="0.65"/>
  <ellipse cx="60" cy="70" rx="40" ry="30" fill="#10b981" opacity="0.5"/>
  <path d="M0 90 Q50 70 100 85 T200 75 L200 120 L0 120Z" fill="#0f766e" opacity="0.4"/>
</svg>
"""

(ASSETS / "mapa-dashboard-heatmap.svg").write_text(DASHBOARD_SVG, encoding="utf-8")
(ASSETS / "mapa-agente-heatmap.svg").write_text(AGENT_SVG, encoding="utf-8")
(ASSETS / "thumb-satelite-heatmap.svg").write_text(THUMB_SAT_SVG, encoding="utf-8")
print("SVG assets created in", ASSETS)
