# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(r"e:\Gi_Pereira\GS - Space Connect\Pitch\Prototipo_EpidemIA.html")

html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EpidemIA — Protótipo</title>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Segoe UI",system-ui,sans-serif;background:#0c1222;color:#e2e8f0;min-height:100vh}
.view{display:none!important;min-height:100vh}
#view-dashboard.view.active{display:flex!important}
#view-agent.view.active{display:flex!important;align-items:center;justify-content:center;padding:24px 16px;background:linear-gradient(180deg,#0f172a,#0c1222)}
.app{display:flex;min-height:100vh;width:100%}
.sidebar{width:240px;background:#111827;border-right:1px solid #1e293b;padding:24px 16px;flex-shrink:0;display:flex;flex-direction:column}
.brand{display:flex;align-items:center;gap:12px;padding:0 8px;margin-bottom:28px}
.brand-icon{width:40px;height:40px;background:linear-gradient(135deg,#3b82f6,#6366f1);border-radius:10px;display:flex;align-items:center;justify-content:center}
.brand h1{font-size:1.35rem;font-weight:700}
.nav{list-style:none;display:flex;flex-direction:column;gap:4px;flex:1}
.nav a{display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:10px;color:#94a3b8;text-decoration:none;font-size:.9rem;font-weight:500}
.nav a.active{background:#3b82f6;color:#fff}
.nav svg{width:20px;height:20px;flex-shrink:0}
.lgpd-side{font-size:.72rem;color:#64748b;line-height:1.4;padding:12px 8px;border-top:1px solid #1e293b;margin-top:auto}
.lgpd-side strong{color:#93c5fd;display:block;margin-bottom:4px}
.main{flex:1;display:flex;flex-direction:column;min-width:0;position:relative}
.main-panel{display:none;flex:1;flex-direction:column;min-width:0}
.main-panel.active{display:flex}
.alert-filters{display:flex;flex-wrap:wrap;gap:8px;padding:0 24px 12px;background:#0f172a;border-bottom:1px solid #1e293b}
.filter-chip{padding:6px 14px;border-radius:999px;border:1px solid #334155;background:#151d2e;color:#94a3b8;font-size:.8rem;font-weight:500;cursor:pointer;font-family:inherit}
.filter-chip:hover,.filter-chip.active{border-color:#3b82f6;color:#e2e8f0;background:rgba(59,130,246,.15)}
.alerts-layout{display:grid;grid-template-columns:1fr 280px;gap:20px;padding:20px 24px;flex:1}
.alert-list{display:flex;flex-direction:column;gap:12px}
.alert-row{background:#151d2e;border:1px solid #1e293b;border-radius:12px;padding:16px 18px;border-left:4px solid #f59e0b;transition:opacity .2s,box-shadow .2s}
.alert-row.crit{border-left-color:#ef4444;background:rgba(239,68,68,.06)}
.alert-row.alto{border-left-color:#f97316}
.alert-row.medio{border-left-color:#fbbf24}
.alert-row.dim{opacity:.45}
.alert-row.highlight{box-shadow:0 0 0 1px rgba(59,130,246,.4)}
.alert-row-head{display:flex;flex-wrap:wrap;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:10px}
.alert-row h4{font-size:.95rem;font-weight:700}
.alert-row .meta{font-size:.75rem;color:#94a3b8}
.alert-badges{display:flex;flex-wrap:wrap;gap:6px}
.badge-ire{font-size:.7rem;font-weight:700;padding:3px 8px;border-radius:999px;background:rgba(239,68,68,.2);color:#fca5a5}
.badge-ire.warn{background:rgba(245,158,11,.2);color:#fcd34d}
.badge-ire.ok{background:rgba(16,185,129,.2);color:#6ee7b7}
.badge-status{font-size:.68rem;font-weight:600;padding:3px 8px;border-radius:999px;text-transform:uppercase;letter-spacing:.03em}
.badge-status.crit{background:#ef4444;color:#fff}
.badge-status.alto{background:#f97316;color:#fff}
.badge-status.medio{background:#f59e0b;color:#0f172a}
.prob-wrap{margin-top:8px}
.prob-label{display:flex;justify-content:space-between;font-size:.72rem;color:#94a3b8;margin-bottom:4px}
.prob-bar{height:6px;background:#1e293b;border-radius:999px;overflow:hidden}
.prob-fill{height:100%;border-radius:999px;background:linear-gradient(90deg,#f59e0b,#ef4444)}
.alert-row-action{font-size:.78rem;color:#cbd5e1;margin-top:10px;padding-top:10px;border-top:1px solid #1e293b}
.alert-side{display:flex;flex-direction:column;gap:12px}
.mini-map-card{background:#151d2e;border:1px solid #1e293b;border-radius:12px;overflow:hidden;position:relative;height:200px}
.mini-map-card .map-ref{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center}
.btn-secondary{display:inline-flex;align-items:center;justify-content:center;width:100%;padding:10px 14px;border:1px solid #334155;border-radius:8px;background:transparent;color:#94a3b8;font-size:.85rem;font-weight:500;cursor:pointer;font-family:inherit}
.btn-secondary:hover{border-color:#3b82f6;color:#e2e8f0}
.alerts-foot{padding:0 24px 20px}
.page-head{padding:16px 24px 12px;border-bottom:1px solid #1e293b;background:#0f172a}
.page-head h2{font-size:1.15rem;font-weight:700}
.page-head h2 span{color:#3b82f6}
.page-sub{font-size:.85rem;color:#94a3b8;margin-top:4px}
.sat-line{font-size:.8rem;color:#10b981;margin-top:8px;display:flex;align-items:center;gap:8px}
.sat-dot{width:8px;height:8px;border-radius:50%;background:#10b981}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;padding:16px 24px;background:#0f172a;border-bottom:1px solid #1e293b}
.kpi{background:#151d2e;border:1px solid #1e293b;border-radius:10px;padding:14px}
.kpi .lbl{font-size:.75rem;color:#94a3b8}
.kpi .val{font-size:1.5rem;font-weight:700;margin-top:4px}
.kpi .val.warn{color:#f59e0b}
.kpi .val.bad{color:#ef4444}
.kpi .val.ok{color:#10b981}
.content{display:grid;grid-template-columns:1fr 300px;gap:20px;padding:20px 24px;flex:1}
.center{display:flex;flex-direction:column;gap:16px}
.map-card{background:#151d2e;border:1px solid #1e293b;border-radius:12px;position:relative;overflow:hidden;width:100%;aspect-ratio:2/1;min-height:280px}
.map-ref{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;display:block}
.pin-main{position:absolute;z-index:4;top:22%;left:38%;transform:translateX(-50%);background:#dc2626;color:#fff;padding:8px 14px;border-radius:8px;font-size:.8rem;font-weight:700;border:2px solid #fff;box-shadow:0 0 24px rgba(239,68,68,.7);animation:pulse 2s infinite}
@keyframes pulse{50%{box-shadow:0 0 32px rgba(239,68,68,.9)}}
.pin-main small{display:block;font-size:.65rem;font-weight:600;opacity:.9;margin-top:2px}
.map-label{position:absolute;z-index:5;background:rgba(0,0,0,.78);color:#fff;font-family:Arial,Helvetica,sans-serif;font-weight:600;line-height:1.35;box-shadow:0 1px 4px rgba(0,0,0,.45);border-radius:3px}
.alert-float{left:14px;top:14px;max-width:300px;padding:6px 10px;font-size:.78rem}
.alert-float strong{display:block;font-size:.82rem;margin-bottom:4px}
.alert-float p{font-size:.72rem;font-weight:500;opacity:.95;margin-bottom:4px}
.ire-pill{display:inline-block;background:rgba(220,38,38,.85);padding:2px 7px;border-radius:2px;font-size:.68rem;font-weight:700}
.map-legend{right:12px;bottom:12px;padding:8px 10px;font-size:.68rem;font-weight:500;max-width:220px}
.map-legend-title{font-weight:700;font-size:.62rem;text-transform:uppercase;margin-bottom:5px;letter-spacing:.02em;line-height:1.25}
.map-legend-row{display:flex;align-items:center;gap:7px;margin-bottom:3px}
.map-legend-row:last-child{margin-bottom:0}
.map-legend-sq{width:11px;height:11px;border:1px solid rgba(0,0,0,.6);flex-shrink:0}
.alerts-panel{background:#151d2e;border:1px solid #1e293b;border-radius:12px;padding:16px}
.alerts-panel h3{font-size:.9rem;margin-bottom:12px}
.alert-card{padding:12px;border-radius:8px;margin-bottom:8px;font-size:.8rem;border-left:4px solid #f59e0b;background:rgba(245,158,11,.08)}
.alert-card.crit{border-left-color:#ef4444;background:rgba(239,68,68,.1)}
.alert-card h4{font-size:.85rem;margin-bottom:4px}
.alert-card p{color:#94a3b8;line-height:1.35}
.actions{background:#151d2e;border:1px solid #1e293b;border-radius:12px;padding:18px 20px}
.actions h3{font-size:.9rem;margin-bottom:10px}
.actions ul{list-style:none;font-size:.85rem;color:#cbd5e1}
.actions li{padding:5px 0 5px 14px;position:relative}
.actions li::before{content:"\\2022";position:absolute;left:0;color:#3b82f6}
.btn-nav{display:inline-flex;align-items:center;justify-content:center;gap:8px;width:100%;margin-top:12px;padding:12px 16px;border:0;border-radius:8px;background:#3b82f6;color:#fff;font-size:.9rem;font-weight:600;cursor:pointer;font-family:inherit}
.btn-nav:hover{background:#2563eb}
.data-panel{background:#151d2e;border:1px solid #1e293b;border-radius:12px;padding:16px;display:flex;flex-direction:column;gap:10px}
.data-panel h3{font-size:.9rem;padding-bottom:8px;border-bottom:1px solid #1e293b}
.metric{background:#0f172a;border:1px solid #1e293b;border-radius:10px;padding:11px 12px}
.mh{display:flex;align-items:flex-start;gap:10px;margin-bottom:6px}
.mico{width:32px;height:32px;background:#1e293b;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:.95rem}
.ml{font-size:.67rem;color:#94a3b8}
.mv{font-size:.88rem;font-weight:700}
.arr{font-size:.7rem;font-weight:700;margin-left:auto}
.arr.up{color:#10b981}
.spark{height:30px;margin-top:4px}
.spark path{fill:none;stroke:#3b82f6;stroke-width:2;filter:drop-shadow(0 0 5px rgba(59,130,246,.6))}
.foot-badge{position:fixed;bottom:10px;left:50%;transform:translateX(-50%);background:rgba(59,130,246,.12);border:1px solid rgba(59,130,246,.3);color:#93c5fd;padding:6px 14px;border-radius:999px;font-size:.7rem;z-index:50}
.agent-wrap{width:100%;max-width:420px}
.agent-top{display:flex;justify-content:space-between;align-items:center;width:100%;max-width:390px;margin:0 auto 16px}
.btn-back{padding:8px 14px;border:1px solid #334155;border-radius:8px;background:transparent;color:#94a3b8;font-size:.85rem;cursor:pointer;font-family:inherit}
.btn-back:hover{border-color:#3b82f6;color:#e2e8f0}
.phone{width:100%;max-width:390px;background:#111827;border:2px solid #1e293b;border-radius:28px;overflow:hidden;box-shadow:0 24px 48px rgba(0,0,0,.45)}
.phone-notch{height:26px;background:#0a0f1a;display:flex;align-items:center;justify-content:center}
.phone-notch span{width:72px;height:5px;background:#1e293b;border-radius:999px}
.phone-body{padding:18px}
.phone-body h2{font-size:1rem;margin-bottom:12px}
.agent-map{height:140px;border-radius:10px;position:relative;margin-bottom:12px;overflow:hidden;background:#0f172a}
.agent-map .map-ref{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.agent-pin{position:absolute;left:48%;top:42%;z-index:3;width:28px;height:28px;background:#ef4444;border:3px solid #fff;border-radius:50% 50% 50% 0;transform:rotate(-45deg);box-shadow:0 2px 8px rgba(0,0,0,.4)}
.coords{font-family:ui-monospace,monospace;font-size:.78rem;background:#0f172a;padding:10px;border-radius:8px;margin-bottom:12px}
.coords .lbl{font-size:.65rem;color:#94a3b8;margin-bottom:4px;font-family:inherit}
.mission{border:1px solid #ef4444;background:rgba(239,68,68,.08);border-radius:10px;padding:14px}
.mission .tag{display:inline-block;background:rgba(239,68,68,.25);color:#fca5a5;font-size:.7rem;font-weight:700;padding:3px 8px;border-radius:999px;margin-bottom:8px}
.mission h3{font-size:.95rem;margin-bottom:6px}
.mission p{font-size:.82rem;color:#94a3b8;line-height:1.4}
.chk{list-style:none;margin-top:12px;font-size:.85rem}
.chk li{padding:8px 0;border-bottom:1px solid #1e293b;display:flex;gap:8px;align-items:center}
.chk li:last-child{border:0}
@media(max-width:1000px){.content{grid-template-columns:1fr}.kpis{grid-template-columns:1fr 1fr}.alerts-layout{grid-template-columns:1fr}.alert-side{display:none}}
</style>
</head>
<body>

<section id="view-dashboard" class="view active">
<div class="app">
<aside class="sidebar">
<div class="brand">
<div class="brand-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/></svg></div>
<h1>EpidemIA</h1>
</div>
<ul class="nav">
<li><a href="#" class="active" data-nav="dashboard"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg><span>Dashboard</span></a></li>
<li><a href="#" data-nav="alertas"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/></svg><span>Alertas de Surtos</span></a></li>
</ul>
<div class="lgpd-side"><strong>LGPD</strong>Dados geoespaciais por zona — nenhum dado pessoal de cidadãos é exposto.</div>
</aside>
<div class="main">
<div id="panel-dashboard" class="main-panel active">
<header class="page-head">
<h2>Dashboard de Controle — <span>São Paulo, SP</span></h2>
<p class="page-sub">Saúde preditiva: dengue, zika e malária · De reativa para preditiva</p>
<p class="sat-line"><span class="sat-dot"></span> Dados satélite: atualizado há 12 min · Motor IRE ativo</p>
</header>
<div class="kpis">
<div class="kpi"><div class="lbl">IRE médio municipal (0–100)</div><div class="val warn">47</div></div>
<div class="kpi"><div class="lbl">Alertas ativos</div><div class="val bad">4</div></div>
<div class="kpi"><div class="lbl">Regiões monitoradas</div><div class="val">18</div></div>
<div class="kpi"><div class="lbl">Ações preventivas (semana)</div><div class="val ok">23</div></div>
</div>
<div class="content">
<div class="center">
<div class="map-card">
<img class="map-ref" src="assets/mapa-heatmap-sp.jpg" alt="Mapa de calor — risco de proliferação de vetores, São Paulo">
<div class="map-label alert-float">
<strong>Quadrante 12A — Zona Norte</strong>
<p>85% de chance de surto nas próximas 3 semanas</p>
<span class="ire-pill">IRE 92 · Crítico</span>
</div>
<div class="pin-main">Quadrante 12A<small>IRE 92</small></div>
<div class="map-label map-legend">
<div class="map-legend-title">Legenda de risco de proliferação de vetores</div>
<div class="map-legend-row"><span class="map-legend-sq" style="background:#22c55e"></span> Baixo risco</div>
<div class="map-legend-row"><span class="map-legend-sq" style="background:#eab308"></span> Médio risco</div>
<div class="map-legend-row"><span class="map-legend-sq" style="background:#ef4444"></span> Alto risco (crítico)</div>
</div>
</div>
<div class="actions">
<h3>Ações recomendadas</h3>
<ul>
<li>Mutirão + fumacê preventivo no Quadrante 12A (48h)</li>
<li>Telemetria orbital — reforço de vigilância Q12A</li>
<li>Drenagem preventiva — Bairro Santana</li>
</ul>
</div>
</div>
<aside class="data-panel">
<h3>Módulo de dados orbitais</h3>
<div class="metric">
<div class="mh"><div class="mico">&#127777;</div><div><div class="ml">Temperatura superfície (EO)</div><div class="mv">26,5°C</div></div><span class="arr up">&#8593;</span></div>
<svg class="spark" viewBox="0 0 120 30" preserveAspectRatio="none"><path d="M0 22 L40 14 L80 18 L120 10"/></svg>
</div>
<div class="metric">
<div class="mh"><div class="mico">&#128167;</div><div><div class="ml">Umidade do solo</div><div class="mv">78% <span style="font-weight:400;color:#94a3b8;font-size:.72rem">ideal</span></div></div></div>
<svg class="spark" viewBox="0 0 120 30" preserveAspectRatio="none"><path d="M0 8 L60 16 L120 12"/></svg>
</div>
<div class="metric">
<div class="mh"><div class="mico">&#129440;</div><div><div class="ml">Risco dengue/zika/malária</div><div class="mv" style="color:#fca5a5">89% <span style="font-weight:400;color:#94a3b8;font-size:.72rem">3 sem.</span></div></div><span class="arr up">&#8593;</span></div>
<svg class="spark" viewBox="0 0 120 30" preserveAspectRatio="none"><path d="M0 24 L40 18 L80 10 L120 4"/></svg>
</div>
<div class="alerts-panel" style="margin-top:4px">
<h3>Alertas por região</h3>
<div class="alert-card crit">
<h4>Quadrante 12A — IRE 92</h4>
<p>85% probabilidade · surto em 3 semanas</p>
</div>
<div class="alert-card">
<h4>Vila Industrial — IRE 71</h4>
<p>62% · janela 4 semanas</p>
</div>
</div>
<button type="button" class="btn-nav" data-show="view-agent">Visão do agente em campo</button>
</aside>
</div>
</div>

<div id="panel-alertas" class="main-panel">
<header class="page-head">
<h2>Alertas de Surtos — <span>São Paulo, SP</span></h2>
<p class="page-sub">Surtos preditivos · dengue, zika e malária</p>
<p class="sat-line"><span class="sat-dot"></span> Dados satélite: atualizado há 12 min · Motor IRE ativo</p>
</header>
<div class="kpis">
<div class="kpi"><div class="lbl">Alertas ativos</div><div class="val bad">4</div></div>
<div class="kpi"><div class="lbl">Críticos (IRE &ge; 71)</div><div class="val bad">2</div></div>
<div class="kpi"><div class="lbl">Probabilidade média de surto</div><div class="val warn">74%</div></div>
<div class="kpi"><div class="lbl">Ações em aberto</div><div class="val">3</div></div>
</div>
<div class="alert-filters">
<button type="button" class="filter-chip active" data-filter="all">Todos</button>
<button type="button" class="filter-chip" data-filter="crit">Crítico</button>
<button type="button" class="filter-chip" data-filter="alto">Alto</button>
<button type="button" class="filter-chip" data-filter="medio">Médio</button>
</div>
<div class="alerts-layout">
<div class="alert-list">
<article class="alert-row crit" data-severity="crit">
<div class="alert-row-head">
<div>
<h4>Quadrante 12A — Zona Norte</h4>
<p class="meta">Detectado há 2h · janela 3 semanas</p>
</div>
<div class="alert-badges">
<span class="badge-ire">IRE 92</span>
<span class="badge-status crit">Crítico</span>
</div>
</div>
<div class="prob-wrap">
<div class="prob-label"><span>Probabilidade de surto</span><span>85%</span></div>
<div class="prob-bar"><div class="prob-fill" style="width:85%"></div></div>
</div>
<p class="alert-row-action">Ação sugerida: mutirão + fumacê preventivo em 48h</p>
</article>
<article class="alert-row alto" data-severity="alto">
<div class="alert-row-head">
<div>
<h4>Vila Industrial</h4>
<p class="meta">Detectado há 5h · janela 4 semanas</p>
</div>
<div class="alert-badges">
<span class="badge-ire warn">IRE 71</span>
<span class="badge-status alto">Alto</span>
</div>
</div>
<div class="prob-wrap">
<div class="prob-label"><span>Probabilidade de surto</span><span>62%</span></div>
<div class="prob-bar"><div class="prob-fill" style="width:62%"></div></div>
</div>
<p class="alert-row-action">Reforço de vigilância e vistoria de criadouros</p>
</article>
<article class="alert-row medio" data-severity="medio">
<div class="alert-row-head">
<div>
<h4>Quarteirão Q12A</h4>
<p class="meta">Detectado há 8h · janela 5 semanas</p>
</div>
<div class="alert-badges">
<span class="badge-ire warn">IRE 68</span>
<span class="badge-status medio">Médio</span>
</div>
</div>
<div class="prob-wrap">
<div class="prob-label"><span>Probabilidade de surto</span><span>55%</span></div>
<div class="prob-bar"><div class="prob-fill" style="width:55%"></div></div>
</div>
<p class="alert-row-action">Telemetria orbital — reforço de monitoramento</p>
</article>
<article class="alert-row medio" data-severity="medio">
<div class="alert-row-head">
<div>
<h4>Bairro Casa Verde</h4>
<p class="meta">Detectado há 1 dia · janela 6 semanas</p>
</div>
<div class="alert-badges">
<span class="badge-ire ok">IRE 58</span>
<span class="badge-status medio">Médio</span>
</div>
</div>
<div class="prob-wrap">
<div class="prob-label"><span>Probabilidade de surto</span><span>41%</span></div>
<div class="prob-bar"><div class="prob-fill" style="width:41%"></div></div>
</div>
<p class="alert-row-action">Drenagem preventiva — Bairro Casa Verde</p>
</article>
</div>
<aside class="alert-side">
<div class="mini-map-card">
<img class="map-ref" src="assets/mapa-heatmap-sp.jpg" alt="Mapa de calor — São Paulo">
</div>
<button type="button" class="btn-secondary" data-nav="dashboard">Ver no mapa principal</button>
</aside>
</div>
<div class="alerts-foot">
<button type="button" class="btn-nav" data-show="view-agent">Visão do agente em campo</button>
</div>
</div>
</div>
</div>
</section>

<section id="view-agent" class="view">
<div class="agent-wrap">
<div class="agent-top">
<button type="button" class="btn-back" data-show="view-dashboard">&larr; Voltar ao dashboard</button>
<span style="font-size:.8rem;color:#94a3b8">Agente · Campo</span>
</div>
<div class="phone">
<div class="phone-notch"><span></span></div>
<div class="phone-body">
<h2>Missão preventiva</h2>
<div class="agent-map"><img class="map-ref" src="assets/mapa-agente-sp.jpg" alt="Mapa — Quadrante 12A"><div class="agent-pin"></div></div>
<div class="coords">
<div class="lbl">Coordenadas GPS — atuação</div>
Lat: -23.5010 · Long: -46.6290<br>
<span style="color:#94a3b8">Zona Norte — Quadrante 12A</span>
</div>
<div class="mission">
<span class="tag">Prioridade alta · IRE 92</span>
<h3>Ação preventiva — Quadrante 12A</h3>
<p>85% probabilidade de surto em 21 dias. Atuar antes da notificação de casos (dengue/zika).</p>
<ul class="chk">
<li>&#9744; Vistoria água parada e criadouros</li>
<li>&#9744; Aplicação de larvicida</li>
<li>&#9744; Registro fotográfico no local</li>
<li>&#9744; Sincronizar visita concluída</li>
</ul>
</div>
</div>
</div>
</div>
</section>

<p class="foot-badge">Protótipo visual — EpidemIA · Space Connect FIAP · LGPD por zona</p>

<script>
(function(){
  function showPanel(name){
    document.querySelectorAll(".main-panel").forEach(function(p){p.classList.remove("active");});
    var panel=document.getElementById("panel-"+name);
    if(panel)panel.classList.add("active");
    document.querySelectorAll(".nav a[data-nav]").forEach(function(a){
      a.classList.toggle("active",a.getAttribute("data-nav")===name);
    });
    window.scrollTo(0,0);
  }
  function showView(id){
    document.querySelectorAll(".view").forEach(function(v){v.classList.remove("active");});
    document.getElementById(id).classList.add("active");
    if(id==="view-dashboard")showPanel("dashboard");
    window.scrollTo(0,0);
  }
  document.querySelectorAll("[data-nav]").forEach(function(el){
    el.addEventListener("click",function(e){
      e.preventDefault();
      var nav=el.getAttribute("data-nav");
      if(nav==="dashboard"||nav==="alertas")showPanel(nav);
    });
  });
  document.querySelectorAll("[data-show]").forEach(function(btn){
    btn.addEventListener("click",function(){showView(btn.getAttribute("data-show"));});
  });
  document.querySelectorAll(".filter-chip").forEach(function(chip){
    chip.addEventListener("click",function(){
      document.querySelectorAll(".filter-chip").forEach(function(c){c.classList.remove("active");});
      chip.classList.add("active");
      var f=chip.getAttribute("data-filter");
      document.querySelectorAll(".alert-row").forEach(function(row){
        var s=row.getAttribute("data-severity");
        var match=f==="all"||f===s;
        row.classList.toggle("dim",!match);
        row.classList.toggle("highlight",match&&f!=="all");
      });
    });
  });
})();
</script>
</body>
</html>"""

# Fix bullet escape in CSS - use actual bullet in Python string
html = html.replace('content:"\\\\2022"', 'content:"•"')

import base64
import mimetypes
import re

def embed_images(html_content, base_dir):
    def replacer(match):
        img_path = match.group(1)
        full_path = base_dir / img_path
        if full_path.exists():
            mime_type, _ = mimetypes.guess_type(str(full_path))
            if not mime_type:
                mime_type = "image/png"
            with open(full_path, "rb") as f:
                b64_data = base64.b64encode(f.read()).decode("utf-8")
            return f'src="data:{mime_type};base64,{b64_data}"'
        return match.group(0)
    return re.sub(r'src="(assets/[^"]+)"', replacer, html_content)

html = embed_images(html, p.parent)

p.write_text(html, encoding="utf-8", newline="\n")
print("OK", p.stat().st_size, "bytes")
