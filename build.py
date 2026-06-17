#!/usr/bin/env python3
"""Build the KOL Series before/after revision workspace (wf-gated).
Re-run after editing SECTIONS[*]['updated'] to regenerate site/index.html."""
import os, base64, json
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes

PASSWORD = "wf"
ITERATIONS = 100_000
HERE = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------------
# SECTIONS: original = Cathy v2 copy (verbatim). updated = filled from Steven's
# input (None until he drops it -> renders "Awaiting your input").
# ----------------------------------------------------------------------------
SECTIONS = [
 {"id":"exec","title":"Executive summary","updated":None,"original":"""
<p>This is a proposal for a new short-form video series built around local sourcing operators. In each market we partner with one verified, credible business owner who sources and sells for a living. They share their own story first to build trust, then walk through how they actually find suppliers and move money across borders. WorldFirst appears mid-story as the tool that solves the payment moment, not as an end-of-video ad read.</p>
<p>Each partner produces one long-form video. From that single shoot we cut four to five vertical shorts. English content runs on WorldFirst channels; local-language content runs on the partner's channels, with collaboration posts where the platform allows it. This gives us reach on both audiences at no extra production cost.</p>
<p>We start with a single-market pilot in the United Kingdom to prove the format, the workflow and the editing pipeline, then scale to Southeast Asia (Singapore, Malaysia, Thailand), followed by European markets (to confirm with the European team) and Australia.</p>
<p>Headline numbers. UK pilot from roughly US$1,000 (one partner, in-house editing) up to about US$1,800 with paid amplification. Full Batch 1 (UK, Southeast Asia, Australia, plus European markets to confirm with the European team) lands at roughly US$6,200 lean, or about US$9,300 with amplification on every market, assuming two European markets. Primary goal: grow reach and lift branded search for WorldFirst in each market.</p>
"""},
 {"id":"concept","title":"The concept","updated":None,"original":"""
<p>The series turns sourcing knowledge into trust. Most sourcing content online is either a faceless explainer or a hard sell. Ours is a real operator letting the audience behind the curtain of their own business. That credibility is the product.</p>
<p class="lbl">The narrative arc (every episode)</p>
<ul>
<li><b>Hook.</b> A surprising or hard-won moment from the operator's own experience: a barrier they hit, a deal that nearly went wrong, the thing nobody warned them about. Pulled from real sourcing stories, with China sourcing preferred.</li>
<li><b>The operator's story.</b> Who they are, how they started, and the expensive mistake they learned from. This is the trust layer.</li>
<li><b>The sourcing walk-through.</b> Where they actually buy: platforms like 1688, Alibaba and AliExpress, local wholesale markets, and factory-direct. How they went from sourcing from a platform to sourcing from factories directly.</li>
<li><b>The payment moment.</b> The exact point where paying a supplier breaks: yuan-only suppliers, currency loss, slow or blocked transfers. This is where WorldFirst come in.</li>
<li><b>The takeaway.</b> A practical 'source like me' tip the viewer can act on, which also makes a strong standalone short.</li>
</ul>
<p>This arc keeps us in the brand's priority order: value first, then viral, then brand mention. The WorldFirst integration lives inside the most useful moment of the video, so it earns its place instead of interrupting.</p>
<p><b>China sourcing preferred.</b> Most of these operators buy from China regardless of where they sell. Their China sourcing relationship, working across distance, language, time zone and payment, is the connective thread of the series and leads naturally into the World Account and 1688 World Pay moment.</p>
"""},
 {"id":"format","title":"Format and production model","updated":None,"original":"""
<p>One long video per market, repurposed into four to five shorts. We shoot once and harvest many clips, which is where the cost efficiency comes from.</p>
<p class="lbl">The shorts breakdown (from one long video)</p>
<table><thead><tr><th>#</th><th>Short</th><th>What it is</th></tr></thead><tbody>
<tr><td>1</td><td class="nw">The barrier hook</td><td>A surprising obstacle or turning point from the operator's own China sourcing story. The scroll-stopper and the series' front door.</td></tr>
<tr><td>2</td><td class="nw">The operator's story</td><td>Origin. 'I run..., heres how I started'. Highest trust-builder, strong for saves and comments.</td></tr>
<tr><td>3</td><td class="nw">Platform walk-through</td><td>How and where they source, real factory versus trader. Pure educational value.</td></tr>
<tr><td>4</td><td class="nw">The payment wall</td><td>Where paying the supplier breaks and how WorldFirst fixes it. The product-led clip.</td></tr>
<tr><td>5</td><td class="nw">Source-like-me playbook</td><td>The practical action tip.</td></tr>
</tbody></table>
<p class="lbl">Extra angles we can layer in</p>
<ul>
<li><b>The mistake reel:</b> the expensive sourcing lesson (scams, bad samples, MOQ traps).</li>
<li><b>Country versus country:</b> what the operator sources from China, locally, or another country, and why.</li>
<li><b>Cost teardown:</b> the full landed cost of one product broken down on screen.</li>
<li><b>Myth-busting:</b> does cheaper at source mean worse quality? Behind-the-scenes at a warehouse or market.</li>
</ul>
<p class="lbl">Built-in depth (how we avoid surface-level content)</p>
<ul>
<li><b>An insider-detail bar:</b> two to three specifics most guides skip (the golden sample trap, the 1688 price floor check, MOQ and mould or sample fees), drawn from the operator.</li>
<li><b>Receipts on screen:</b> real invoices, anonymised supplier chats and payment screenshots, product in hand. Proof over claims.</li>
<li><b>Recurring signature segments / one shared question per operator:</b> repeatable beats that give the series an identity, each answers the same question (for example, the biggest mistake that cost me... what would you tell yourself before your first sourcing order), creating a comparable thread across markets and an easy compilation later.</li>
</ul>
<p class="lbl">Language and distribution</p>
<table><thead><tr><th>Content</th><th>Where it goes</th></tr></thead><tbody>
<tr><td class="nw">English content</td><td>WorldFirst channels (Instagram, TikTok, YouTube, Facebook).</td></tr>
<tr><td class="nw">Local-language content</td><td>The partner/kol's own channels, where their audience and trust already live.</td></tr>
<tr><td class="nw"></td><td>Collaboration or co-posts so one piece reaches both audiences. Decided case by case per partner.</td></tr>
</tbody></table>
<p><b>Editing.</b> WorldFirst edits by default, which keeps brand consistency. If a partner prefers to edit their own cuts, we co-edit and supply brand guidelines, and the WorldFirst integration brief.</p>
<p><b>Usage rights.</b> Every partner agreement grants WorldFirst rights to repurpose the footage into shorts and to boost the best clips with paid spend.</p>
"""},
 {"id":"markets","title":"Markets and rollout","updated":None,"original":"""
<p>UK first as a true pilot, then scale in waves. Each market uses one local verified operator who runs their own sourcing or selling business.</p>
<table><thead><tr><th>Wave</th><th>Markets</th><th>Why this order</th><th>Content language</th></tr></thead><tbody>
<tr><td class="nw">Pilot</td><td>United Kingdom</td><td>English-first, mature WorldFirst market, prove the format and pipeline once.</td><td>English on WorldFirst channels</td></tr>
<tr><td class="nw">Wave 2</td><td>Singapore, Malaysia, Thailand</td><td>Southeast Asia is a priority growth market for the business.</td><td>Local languages on partner channels</td></tr>
<tr><td class="nw">Wave 3</td><td>Europe (e.g. Germany, Poland)</td><td>Anchor European markets. Final mix to be confirmed with Scarlett, European Marketing Manager.</td><td>Local language on partner channels</td></tr>
<tr><td class="nw">Wave 4</td><td>Australia</td><td>English-first, familiar market, rounds out Batch 1.</td><td>English on WorldFirst channels</td></tr>
</tbody></table>
"""},
 {"id":"partner","title":"Partner selection and vetting","updated":None,"original":"""
<p>The series lives or dies on partner credibility. We screen every candidate against a fixed rubric before any agreement.</p>
<ul>
<li><b>Runs a real business.</b> A verifiable importing, e-commerce or sourcing operation: a registered business, an active store, and a track record we can confirm.</li>
<li><b>First-hand sourcing experience.</b> They can tell genuine stories, including the mistakes, not recite generic tips.</li>
<li><b>Audience overlap.</b> Their followers skew toward importers and cross-border sellers, our two core audiences.</li>
<li><b>Engagement over follower count.</b> Saves, comments and watch-time matter more than raw reach. A smaller, engaged niche audience beats a large passive one.</li>
<li><b>On-camera credibility.</b> Clear delivery in English for English content, or strong native delivery for local-language content.</li>
<li><b>Brand-safe and conflict-free.</b> Not currently promoting a competing cross-border payment product, and comfortable integrating WorldFirst authentically mid-story.</li>
</ul>
"""},
 {"id":"kpis","title":"Goals and KPIs","updated":None,"original":"""
<p><b>Primary goal:</b> grow reach and lift branded search for WorldFirst in each market. In plain terms, more of the right people see the content, and more of them go on to search for WorldFirst and the World Account.</p>
<p>We do not set one fixed view target across partners, because reach scales with each partner's audience. A small, highly engaged operator and a large one will never post the same numbers. So each partner is judged against their own baseline and on rates and efficiency.</p>
<p class="lbl">Layer 1: each partner against their own baseline</p>
<p>Before signing, we record the partner's recent norm (median views and engagement on their last 10 to 20 posts). Success is the WorldFirst piece performing at or above that median, ideally in their top quartile.</p>
<p class="lbl">Layer 2: efficiency, so different-sized partners compare fairly</p>
<table><thead><tr><th>Metric</th><th>What it tells us</th></tr></thead><tbody>
<tr><td class="nw">Cost per 1,000 views (CPM)</td><td>Raw reach value for money.</td></tr>
<tr><td class="nw">Cost per save</td><td>Value of high-intent interest.</td></tr>
<tr><td class="nw">Cost per profile or link click</td><td>Value of traffic driven.</td></tr>
<tr><td class="nw">Cost per World Account signup</td><td>Direct business value. Pairs with the affiliate deal.</td></tr>
</tbody></table>
<p class="lbl">Layer 3: brand outcomes (independent of partner size)</p>
<table><thead><tr><th>Metric</th><th>How measured</th></tr></thead><tbody>
<tr><td class="nw">Branded search lift (WorldFirst, World Account)</td><td>Google Trends in-market, plus branded and direct site traffic.</td></tr>
<tr><td class="nw">New WorldFirst followers</td><td>Platform analytics.</td></tr>
<tr><td class="nw">World Account signups or referral-code uses</td><td>UTM links, referral codes.</td></tr>
<tr><td class="nw">English content on WorldFirst channels</td><td>Beat our own channel median for views and saves.</td></tr>
</tbody></table>
"""},
 {"id":"timeline","title":"Timeline","updated":None,"original":"""
<p>A focused UK pilot, a deliberate readout, then staged expansion. Indicative weeks from a late-June 2026 start.</p>
<table><thead><tr><th>Phase</th><th>Timing</th><th>Focus</th><th>Key outputs</th></tr></thead><tbody>
<tr><td class="nw">0. Foundation</td><td>Weeks 1 (Mid Jun)</td><td>Set up the system before spending on talent.</td><td>Brief and rights templates, KPI baseline captured.</td></tr>
<tr><td class="nw">1. UK pilot</td><td>Weeks 2-7 (Late Jun-July)</td><td>Shortlist and vet, contract, pre-production, shoot, edit, publish.</td><td>One long video plus four to five shorts, live on channel.</td></tr>
<tr><td class="nw">2. Pilot readout</td><td>Week 8 (early Aug)</td><td>Measure against KPIs, refine the playbook.</td><td>Results memo and a tightened repeatable workflow.</td></tr>
<tr><td class="nw">3. SEA wave</td><td>Weeks 9-16 (Aug-Sep)</td><td>Singapore, then Malaysia, then Thailand, staggered.</td><td>Three markets live, local-language partner posts.</td></tr>
<tr><td class="nw">4. Europe + Australia</td><td>Weeks 17-24 (Sep-Nov)</td><td>European markets (with Scarlett) plus Australia.</td><td>Batch 1 complete across all markets.</td></tr>
</tbody></table>
<p>Staggering one market at a time keeps coordination and editing load manageable and lets each market learn from the last.</p>
"""},
 {"id":"budget","title":"Budget","updated":None,"original":"""
<p>Partner fees are benchmarked against current 2026 creator rates for credible micro-tier creators (roughly 10,000 to 100,000 followers) with a business or B2B niche, which commands a premium over general lifestyle creators. Asia-Pacific rates run lower than the UK, Germany and Australia. Figures are in US dollars for comparison.</p>
<p class="lbl">Benchmarked partner fee per market. One package = one long-form shoot, rights to cut four to five shorts</p>
<table><thead><tr><th>Market</th><th>Planning rate</th><th>Range</th><th>Note</th></tr></thead><tbody>
<tr><td class="nw">United Kingdom</td><td>US$2,000</td><td>US$1,000 - 2,500</td><td>English, WorldFirst channels</td></tr>
<tr><td class="nw">Singapore</td><td>US$1,000</td><td>US$600 - 1,500</td><td>Highest within SEA</td></tr>
<tr><td class="nw">Malaysia</td><td>US$800</td><td>US$300 - 1,000</td><td>Lower cost market</td></tr>
<tr><td class="nw">Thailand</td><td>US$800</td><td>US$300 - 1,000</td><td>Lower cost market</td></tr>
<tr><td class="nw">Germany</td><td>US$1,500</td><td>US$1,000 - 2,500</td><td>Europe, Western rates</td></tr>
<tr><td class="nw">Poland</td><td>US$1,500</td><td>US$1,000 - 2,000</td><td>Europe, Eastern, lower cost (estimate, to confirm)</td></tr>
<tr><td class="nw">Australia</td><td>US$1,000</td><td>US$1,000 - 2,000</td><td>Roughly AUD 1,100 - 2,400</td></tr>
<tr><td class="nw">Full Batch 1 (~7 markets)</td><td>~US$8,600</td><td>~US$12,500</td><td>UK, SEA x3, Australia, plus 2 European (count TBC with Scarlett)</td></tr>
</tbody></table>
"""},
]

def encrypt_payload(plaintext, password=PASSWORD):
    salt = os.urandom(16); iv = os.urandom(12)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITERATIONS)
    key = kdf.derive(password.encode("utf-8"))
    ct = AESGCM(key).encrypt(iv, plaintext.encode("utf-8"), None)
    return {"v":1,"salt":base64.b64encode(salt).decode(),"iv":base64.b64encode(iv).decode(),
            "iterations":ITERATIONS,"ciphertext":base64.b64encode(ct).decode()}

def build_inner():
    secs = []
    for i, s in enumerate(SECTIONS, 1):
        if s["updated"]:
            upd = f'<div class="body">{s["updated"]}</div>'
            ucls = "updated has"
        else:
            upd = '<div class="pending">Awaiting your input</div>'
            ucls = "updated"
        secs.append(f"""
<section class="sec" id="sec-{s['id']}">
  <div class="sechead"><span class="n">{i:02d}</span><h2>{s['title']}</h2></div>
  <div class="cols">
    <div class="col">
      <div class="collbl">Original &middot; Cathy v2</div>
      <div class="body orig">{s['original']}</div>
    </div>
    <div class="col">
      <div class="collbl">Your input</div>
      <textarea class="inp" data-sid="{s['id']}" placeholder="drop your notes / direction for this section here"></textarea>
    </div>
  </div>
  <div class="{ucls}">
    <div class="collbl">Updated</div>
    {upd}
  </div>
</section>""")
    return f"""
<header class="page">
  <div class="eyebrow">Revision workspace</div>
  <h1>Localised Sourcing KOL Video Series</h1>
  <p class="sub">Original (Cathy v2) on the left, your input on the right. I rebuild the Updated copy from your input, section by section.</p>
  <p class="how">Type into any <b>Your input</b> box (saved on this device as you go), then hit <b>Copy all my input</b> at the bottom and paste it back to me. Or just tell me in chat. The Updated panels fill in once your input lands.</p>
  <div class="meta">Source: Localised Sourcing KOL Series Project Plan_v2.docx &middot; prepared 2026-06-16 &middot; <a href="#" onclick="localStorage.removeItem('kolrev_pw');location.reload();return false;">lock device</a></div>
</header>
{''.join(secs)}
<div class="foot">
  <button id="copybtn" type="button">Copy all my input</button>
  <span id="copymsg"></span>
  <a class="lock" href="#" onclick="localStorage.removeItem('kolrev_pw');location.reload();return false;">lock device</a>
</div>
"""

CSS = """
:root{--ink:#111114;--ink2:#3a3a40;--ink3:#6b6b73;--ink4:#9a9aa2;--line:#e7e7ea;--line2:#f0f0f2;--bg:#fff;--bg2:#fafafa;}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif;font-size:15px;line-height:1.6;-webkit-font-smoothing:antialiased;padding:56px 40px 140px}
body.locked #content{display:none}
#content{max-width:1180px;margin:0 auto}
.eyebrow{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink4);margin-bottom:12px}
header.page{padding-bottom:34px;border-bottom:1px solid var(--line);margin-bottom:14px}
h1{font-size:30px;line-height:1.18;letter-spacing:-.018em;font-weight:680;margin-bottom:14px}
.sub{font-size:16px;color:var(--ink2);max-width:760px;margin-bottom:14px}
.how{font-size:13.5px;color:var(--ink3);max-width:760px;background:var(--bg2);border:1px solid var(--line);border-radius:10px;padding:12px 15px}
.how b{color:var(--ink)}
.meta{font-size:12.5px;color:var(--ink4);margin-top:16px}
.meta a,.lock{color:var(--ink4);text-decoration:underline;text-underline-offset:2px}
.sec{margin-top:44px;scroll-margin-top:40px}
.sechead{display:flex;align-items:baseline;gap:12px;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid var(--line)}
.sechead .n{font-size:13px;font-variant-numeric:tabular-nums;color:var(--ink4);font-weight:600}
.sechead h2{font-size:19px;font-weight:660;letter-spacing:-.01em}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:start}
.col{min-width:0}
.collbl{font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink4);font-weight:600;margin-bottom:10px}
.body{font-size:14px;color:var(--ink2)}
.body.orig{background:var(--bg2);border:1px solid var(--line);border-radius:10px;padding:18px 20px}
.body p{margin-bottom:12px}.body p:last-child{margin-bottom:0}
.body b{color:var(--ink);font-weight:620}
.body .lbl{font-weight:620;color:var(--ink);margin-top:16px;font-size:13.5px}
.body ul{margin:4px 0 12px;padding-left:20px}
.body li{margin-bottom:7px}
.body table{width:100%;border-collapse:collapse;margin:10px 0 14px;font-size:13px}
.body th{text-align:left;font-size:10px;letter-spacing:.05em;text-transform:uppercase;color:var(--ink4);font-weight:600;padding:0 10px 7px 0;border-bottom:1px solid var(--line)}
.body td{padding:8px 10px 8px 0;border-bottom:1px solid var(--line2);color:var(--ink2);vertical-align:top}
.body td.nw{color:var(--ink);font-weight:560;white-space:nowrap}
.body tr:last-child td{border-bottom:none}
textarea.inp{width:100%;min-height:200px;resize:vertical;font:inherit;font-size:14px;line-height:1.55;color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:10px;padding:16px 18px;outline:none;transition:border-color .15s}
textarea.inp:focus{border-color:var(--ink3)}
textarea.inp.filled{border-color:var(--ink);background:#fcfcfd}
.updated{margin-top:18px;border:1px solid var(--line);border-radius:10px;padding:16px 20px;background:#fff}
.updated.has{border-color:var(--ink);background:#fcfcfd}
.pending{font-size:13px;color:var(--ink4);font-style:italic}
.foot{margin-top:56px;padding-top:24px;border-top:1px solid var(--line);display:flex;align-items:center;gap:16px}
#copybtn{font:inherit;font-size:14px;font-weight:560;color:#fff;background:var(--ink);border:none;border-radius:8px;padding:11px 20px;cursor:pointer}
#copybtn:hover{background:#000}
#copymsg{font-size:13px;color:var(--ink3)}
.foot .lock{margin-left:auto;font-size:12.5px}
/* gate */
body.locked{display:flex;align-items:center;justify-content:center;min-height:90vh;padding:40px}
#gate-card{max-width:320px;width:100%;text-align:center}
#gate-card h2{font-size:16px;font-weight:600;color:var(--ink2);margin-bottom:18px}
#gate-input{font:inherit;font-size:15px;width:100%;padding:11px 14px;border:1px solid var(--line);border-radius:8px;outline:none;text-align:center}
#gate-input:focus{border-color:var(--ink3)}
#gate-btn{font:inherit;font-size:14px;font-weight:560;color:#fff;background:var(--ink);border:none;border-radius:8px;padding:10px 20px;margin-top:10px;cursor:pointer;width:100%}
#gate-err{font-size:12.5px;color:#c4322a;margin-top:10px;min-height:16px}
@media(max-width:820px){body{padding:32px 18px 100px}.cols{grid-template-columns:1fr;gap:14px}}
"""

SHELL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>KOL Series &middot; Revision Workspace</title>
<style>__CSS__</style>
</head>
<body class="locked">
<div id="gate">
  <div id="gate-card">
    <h2>Localised Sourcing KOL Series &middot; revision</h2>
    <form id="gate-form" onsubmit="return gateSubmit(event)">
      <input id="gate-input" type="password" placeholder="password" autocomplete="off" autofocus>
      <button id="gate-btn" type="submit">Enter</button>
    </form>
    <div id="gate-err"></div>
  </div>
</div>
<div id="content" hidden></div>
<script type="application/json" id="payload">__PAYLOAD__</script>
<script>
function b64ToBytes(b){const s=atob(b),a=new Uint8Array(s.length);for(let i=0;i<s.length;i++)a[i]=s.charCodeAt(i);return a;}
async function deriveKey(p,salt,it){const e=new TextEncoder();const bk=await crypto.subtle.importKey("raw",e.encode(p),"PBKDF2",false,["deriveKey"]);return crypto.subtle.deriveKey({name:"PBKDF2",salt,iterations:it,hash:"SHA-256"},bk,{name:"AES-GCM",length:256},false,["decrypt"]);}
async function decryptPayload(p){const b=JSON.parse(document.getElementById('payload').textContent);const key=await deriveKey(p,b64ToBytes(b.salt),b.iterations);const plain=await crypto.subtle.decrypt({name:"AES-GCM",iv:b64ToBytes(b.iv)},key,b64ToBytes(b.ciphertext));return new TextDecoder().decode(plain);}
function reveal(html){document.getElementById('content').innerHTML=html;document.getElementById('content').hidden=false;document.getElementById('gate').style.display='none';document.body.classList.remove('locked');initApp();}
async function gateSubmit(e){e.preventDefault();const inp=document.getElementById('gate-input'),err=document.getElementById('gate-err');err.textContent='';try{const h=await decryptPayload(inp.value);reveal(h);try{localStorage.setItem('kolrev_pw',inp.value);}catch(_){}}catch(ex){err.textContent='wrong password';inp.value='';inp.focus();}return false;}
function initApp(){
  const tas=[...document.querySelectorAll('textarea.inp')];
  tas.forEach(ta=>{
    const k='kolrev_input_'+ta.dataset.sid;
    try{const v=localStorage.getItem(k);if(v){ta.value=v;ta.classList.add('filled');}}catch(_){}
    ta.addEventListener('input',()=>{try{localStorage.setItem(k,ta.value);}catch(_){}ta.classList.toggle('filled',ta.value.trim().length>0);});
  });
  const btn=document.getElementById('copybtn'),msg=document.getElementById('copymsg');
  if(btn)btn.addEventListener('click',()=>{
    let out='== KOL series revision input ==\\n';
    tas.forEach(ta=>{const sec=ta.closest('.sec');const t=sec.querySelector('h2').textContent;const n=sec.querySelector('.n').textContent;const v=ta.value.trim();out+='\\n['+n+' '+t+']\\n'+(v?v:'(no change)')+'\\n';});
    navigator.clipboard.writeText(out).then(()=>{msg.textContent='copied. paste it back to me.';setTimeout(()=>msg.textContent='',4000);},()=>{msg.textContent='copy failed, select manually';});
  });
}
(async()=>{try{const c=localStorage.getItem('kolrev_pw');if(c)reveal(await decryptPayload(c));}catch(_){try{localStorage.removeItem('kolrev_pw');}catch(_){}}})();
</script>
</body>
</html>
"""

def main():
    inner = build_inner()
    blob = encrypt_payload(inner)
    html = SHELL.replace("__CSS__", CSS).replace("__PAYLOAD__", json.dumps(blob))
    out_dir = os.path.join(HERE, "site")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(html)
    # plaintext check
    leak = any(s["original"].strip()[:40] in html for s in SECTIONS)
    print(f"built site/index.html | {len(html)} chars | password={PASSWORD} | plaintext_leak={leak}")

if __name__ == "__main__":
    main()
