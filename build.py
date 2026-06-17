#!/usr/bin/env python3
"""Build the KOL Series before/after revision workspace (wf-gated).
Left = Cathy v2 (verbatim). Middle-right = Steven's input (captured). Updated = rebuilt from input.
Re-run after editing SECTIONS to regenerate index.html."""
import os, base64, json
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes

PASSWORD = "wf"
ITERATIONS = 100_000
HERE = os.path.dirname(os.path.abspath(__file__))

SECTIONS = [
 {"id":"exec","title":"Executive summary",
  "original":"""
<p>This is a proposal for a new short-form video series built around local sourcing operators. In each market we partner with one verified, credible business owner who sources and sells for a living. They share their own story first to build trust, then walk through how they actually find suppliers and move money across borders. WorldFirst appears mid-story as the tool that solves the payment moment, not as an end-of-video ad read.</p>
<p>Each partner produces one long-form video. From that single shoot we cut four to five vertical shorts. English content runs on WorldFirst channels; local-language content runs on the partner's channels, with collaboration posts where the platform allows it. This gives us reach on both audiences at no extra production cost.</p>
<p>We start with a single-market pilot in the United Kingdom to prove the format, the workflow and the editing pipeline, then scale to Southeast Asia (Singapore, Malaysia, Thailand), followed by European markets (to confirm with the European team) and Australia.</p>
<p>Headline numbers. UK pilot from roughly US$1,000 (one partner, in-house editing) up to about US$1,800 with paid amplification. Full Batch 1 lands at roughly US$6,200 lean, or about US$9,300 with amplification on every market, assuming two European markets. Primary goal: grow reach and lift branded search for WorldFirst in each market.</p>
""",
  "userinput":"""
<ul>
<li>The pinpoint: we have already produced really good sourcing content and occupy that pillar well in English, generically. It aligns with our business direction, segmentation and positioning, and is worth investing in further.</li>
<li>We already tell compelling "source from China" stories, but people trust their local voice and their own language.</li>
<li>Our past China-sourcing stories are the tip of the iceberg: the English-fluent crowd already sees and likes our content. But huge segments only trust people in their own communities and countries, even if they speak English.</li>
<li>The opportunity: move from generic "how to source from China" to specific "how to source from China for the UK", etc. That captures the real intent of each key market with a localised voice, instead of one collective English speaker.</li>
<li>Combine these angles together. Keep it active and tips-led.</li>
</ul>
""",
  "updated":"""
<p>WorldFirst already produces strong sourcing-from-China content, and we occupy that pillar well in English. It performs, it aligns with our business direction, segmentation and positioning, and it is worth investing in further. The real gap is who it reaches.</p>
<p>Our best China-sourcing stories today are the tip of the iceberg. They land with audiences who are comfortable in generic English content and already like what we make. But large segments in our key markets only trust voices from their own country and community, in their own language and accent, even when they also speak English. A single collective English voice cannot reach them.</p>
<p>That is the opportunity. We move from one generic "how to source from China" to specific, local versions of the same story: how to source from China for the UK, for Germany, for Vietnam. The moment the story gets that specific, it captures the real intent of each market and is told by a voice that market actually trusts. Same proven pillar, localised, reaching the people the generic version never could.</p>
<p>The series makes this repeatable: one credible local operator per market, telling their own first-hand China-sourcing story, with the WorldFirst payment moment built into the most useful part of the video.</p>
"""},

 {"id":"concept","title":"The concept",
  "original":"""
<p>The series turns sourcing knowledge into trust. Most sourcing content online is either a faceless explainer or a hard sell. Ours is a real operator letting the audience behind the curtain of their own business. That credibility is the product.</p>
<p class="lbl">The narrative arc (every episode)</p>
<ul>
<li><b>Hook.</b> A surprising or hard-won moment from the operator's own experience. Pulled from real sourcing stories, with China sourcing preferred.</li>
<li><b>The operator's story.</b> Who they are, how they started, and the expensive mistake they learned from. This is the trust layer.</li>
<li><b>The sourcing walk-through.</b> Where they actually buy: 1688, Alibaba, AliExpress, local wholesale markets, factory-direct.</li>
<li><b>The payment moment.</b> The exact point where paying a supplier breaks. This is where WorldFirst come in.</li>
<li><b>The takeaway.</b> A practical 'source like me' tip, which also makes a strong standalone short.</li>
</ul>
<p>This arc keeps us in the brand's priority order: value first, then viral, then brand mention.</p>
<p><b>China sourcing preferred.</b> Most operators buy from China regardless of where they sell. That relationship is the connective thread and leads into the World Account and 1688 World Pay moment.</p>
""",
  "userinput":"""
<ul>
<li>Cathy nailed the real-operator story and the payment moment. Keep her flow, it makes sense.</li>
<li>Before vs after: before we had a spokesperson; now it must be a real operator with first-hand China-sourcing experience.</li>
<li>They talk in their own language, accent and specific market context. Not generic English "source from China" but very specific, e.g. sourcing from China into Australia: the problems, difficulties, tariffs, rules, even getting scammed by suppliers, in their local market terms.</li>
<li>A different person every episode: sourcing influencers, real operators, or our clients. We are not hiring "anyone to do sourcing"; we find real experts on one specific country or small region's China sourcing. Regional specificity is the point.</li>
<li>China sourcing is not "preferred", it is a MUST.</li>
<li>Long-form = long-term evergreen content for video SEO and professional presentation. Repurpose ~3 shorts per long-form around the key talking points; shorts carry the wider reach. A blend of depth and reach.</li>
<li>Distribution: English content can still sit on our global channels but co-published with an operator. Non-English sits on the operator's own channel. Can also be a co-brand play (e.g. partner with a professional brand in Germany to co-publish).</li>
</ul>
""",
  "updated":"""
<p>The series turns sourcing knowledge into trust. The two things that make it work, and that we keep from the original, are the real operator story and the payment moment. The narrative arc stays the same: hook, the operator's story, the sourcing walk-through, the payment moment, the takeaway.</p>
<p class="lbl">What changes</p>
<ul>
<li><b>A real operator, not a spokesperson.</b> Every partner must have genuine first-hand China-sourcing experience. This is the before-and-after: we move from a presenter reading our story to an operator telling their own.</li>
<li><b>Local voice, specific market.</b> They speak in their own language and accent, about their own market. Not generic "source from China" but, for example, sourcing from China into Australia: the tariffs, the rules, the supplier scams, the realities of that specific route.</li>
<li><b>A different expert every episode.</b> Sourcing agents, real operators, or our own clients. We are not hiring someone to talk about sourcing in general. We find a real expert on one country or small region's China-sourcing reality. That regional specificity is the point.</li>
<li><b>China sourcing is a must, not a preference.</b> It is the connective thread of every episode and leads into the World Account and 1688 World Pay moment.</li>
</ul>
<p class="lbl">Long-form for depth, shorts for reach</p>
<p>Each long-form video is built as long-term evergreen content: it works for video SEO and stands up as a professional, presentation-grade piece. From every long-form episode we repurpose around three shorts built on the key talking points, and the shorts carry the wider-reach numbers. Depth and reach from one shoot.</p>
<p class="lbl">Distribution</p>
<p>English content can still sit on WorldFirst global channels, but co-published with the operator. Non-English content lives on the operator's own channel, where the audience and trust already are. Either can extend into a co-brand play, for example partnering with a professional company or brand in-market (such as in Germany) to co-publish.</p>
"""},

 {"id":"format","title":"Format and production model",
  "original":"""
<p>One long video per market, repurposed into four to five shorts. We shoot once and harvest many clips, which is where the cost efficiency comes from.</p>
<p class="lbl">The shorts breakdown (from one long video)</p>
<table><thead><tr><th>#</th><th>Short</th><th>What it is</th></tr></thead><tbody>
<tr><td>1</td><td class="nw">The barrier hook</td><td>The scroll-stopper and the series' front door.</td></tr>
<tr><td>2</td><td class="nw">The operator's story</td><td>Origin. Highest trust-builder, strong for saves and comments.</td></tr>
<tr><td>3</td><td class="nw">Platform walk-through</td><td>Real factory versus trader. Pure educational value.</td></tr>
<tr><td>4</td><td class="nw">The payment wall</td><td>Where paying the supplier breaks and how WorldFirst fixes it.</td></tr>
<tr><td>5</td><td class="nw">Source-like-me playbook</td><td>The practical action tip.</td></tr>
</tbody></table>
<p class="lbl">Built-in depth</p>
<p>An insider-detail bar (the golden sample trap, the 1688 price floor check, MOQ and sample fees); receipts on screen (real invoices, anonymised supplier chats, payment screenshots); recurring signature segments with one shared question per operator for a comparable thread across markets.</p>
<p class="lbl">Language and distribution</p>
<p>English content on WorldFirst channels; local-language content on the partner's own channels; collaboration or co-posts case by case. WorldFirst edits by default. Every agreement grants rights to repurpose and to boost the best clips.</p>
""",
  "userinput":"""
<ul>
<li>Cathy already caught this. If nothing is different, just keep her version.</li>
</ul>
""",
  "updated":"""
<p><b>No change. Cathy's format and production model stands.</b></p>
<p class="lbl">One point to settle</p>
<p>Your concept note lands on roughly three shorts per long-form (built around the key talking points), while this format model says four to five. Worth confirming the working number before it goes in: three sharper talking-point shorts, or four to five for volume.</p>
"""},

 {"id":"markets","title":"Markets and rollout",
  "original":"""
<p>UK first as a true pilot, then scale in waves. Each market uses one local verified operator.</p>
<table><thead><tr><th>Wave</th><th>Markets</th><th>Content language</th></tr></thead><tbody>
<tr><td class="nw">Pilot</td><td>United Kingdom</td><td>English on WorldFirst channels</td></tr>
<tr><td class="nw">Wave 2</td><td>Singapore, Malaysia, Thailand</td><td>Local languages on partner channels</td></tr>
<tr><td class="nw">Wave 3</td><td>Europe (e.g. Germany, Poland)</td><td>Local language on partner channels</td></tr>
<tr><td class="nw">Wave 4</td><td>Australia</td><td>English on WorldFirst channels</td></tr>
</tbody></table>
""",
  "userinput":"""
<ul>
<li>Pilot: United Kingdom.</li>
<li>Wave 2: add Vietnam (alongside SEA).</li>
<li>Wave 3: Europe = Germany, Poland, Turkey; plus Australia.</li>
<li>Wave 4: United States and Mexico, plus the rest of the regions.</li>
</ul>
""",
  "updated":"""
<table><thead><tr><th>Wave</th><th>Markets</th><th>Why this order</th><th>Content language</th></tr></thead><tbody>
<tr><td class="nw">Pilot</td><td>United Kingdom</td><td>English-first, mature WorldFirst market. Prove the format and pipeline once.</td><td>English, co-published with operator</td></tr>
<tr><td class="nw">Wave 2</td><td>Singapore, Malaysia, Thailand, Vietnam</td><td>Southeast Asia priority growth. Vietnam added.</td><td>Local languages on operator channels</td></tr>
<tr><td class="nw">Wave 3</td><td>Germany, Poland, Turkey, Australia</td><td>Anchor Europe (mix with Scarlett) plus Australia.</td><td>Local language; Australia English</td></tr>
<tr><td class="nw">Wave 4</td><td>United States, Mexico, and remaining regions</td><td>Larger and later markets, staged last.</td><td>Mixed by market</td></tr>
</tbody></table>
"""},

 {"id":"partner","title":"Partner selection and vetting",
  "original":"""
<p>The series lives or dies on partner credibility. We screen every candidate against a fixed rubric.</p>
<ul>
<li><b>Runs a real business.</b> A verifiable importing, e-commerce or sourcing operation.</li>
<li><b>First-hand sourcing experience.</b> Genuine stories, not generic tips.</li>
<li><b>Audience overlap.</b> Followers skew toward importers and cross-border sellers.</li>
<li><b>Engagement over follower count.</b> Saves, comments and watch-time over raw reach.</li>
<li><b>On-camera credibility.</b> Clear delivery in English or strong native delivery.</li>
<li><b>Brand-safe and conflict-free.</b> Not promoting a competing payment product.</li>
</ul>
""",
  "userinput":"""
<ul>
<li>Must be specific. A sourcing agent working for specific countries, or a business owner who sourced from China for one region.</li>
<li>Must have first-hand sourcing experience.</li>
<li>Must speak credibly to B2B owners or successful e-commerce brand owners, the personas that exactly match our target audience.</li>
</ul>
""",
  "updated":"""
<p>The series lives or dies on partner credibility, and the partner must be specific to a market, not a generalist. We screen every candidate against a fixed rubric before any agreement.</p>
<ul>
<li><b>A country or region specialist.</b> A sourcing agent who works for a specific country, or a business owner who sources from China for one specific market. Not a generic sourcing presenter.</li>
<li><b>First-hand sourcing experience.</b> Real stories, including the mistakes, not recited tips.</li>
<li><b>Speaks to our exact audience.</b> Credible talking to B2B owners and successful e-commerce brand owners, the personas that match our target audience.</li>
<li><b>Runs a real business.</b> A verifiable importing, e-commerce or sourcing operation with a track record we can confirm.</li>
<li><b>Engagement over follower count.</b> Saves, comments and watch-time matter more than raw reach.</li>
<li><b>On-camera credibility.</b> Strong delivery in their own language for local content, or in English for English content.</li>
<li><b>Brand-safe and conflict-free.</b> Not promoting a competing cross-border payment product, and comfortable integrating WorldFirst authentically mid-story.</li>
</ul>
"""},

 {"id":"kpis","title":"Goals and KPIs",
  "original":"""
<p><b>Primary goal:</b> grow reach and lift branded search for WorldFirst in each market.</p>
<p>No single fixed view target across partners. Each partner is judged against their own baseline and on efficiency.</p>
<p class="lbl">Layer 1: each partner against their own baseline</p>
<p>Record the partner's recent norm (median of last 10 to 20 posts). Success is performing at or above that median.</p>
<p class="lbl">Layer 2: efficiency</p>
<p>Cost per 1,000 views (CPM), cost per save, cost per profile or link click, cost per World Account signup.</p>
<p class="lbl">Layer 3: brand outcomes</p>
<p>Branded search lift (Google Trends), new followers, World Account signups or referral-code uses, beating our own channel median.</p>
""",
  "userinput":"""
<ul>
<li>Top line = views (overall reach / impressions / views). Aim for 1,000,000 views per episode (long + shorts combined).</li>
<li>Break down via CPM using existing data, as a reference for Cathy.</li>
<li>Organic vs paid: organic ~20% of total, paid ~80%. Organic CPM is very expensive, paid CPM lower. Monitor both separately.</li>
<li>Three cost lenses: production, organic / partnership distribution, paid. Cost per episode and cost per impression are secondary. Costs are secondary overall.</li>
<li>True engagement rate (our true-engagement index) is a primary goal, across the organic then the paid period.</li>
<li>Viral target: ~1 viral piece per episode. Viral = 10,000 organic views with over 2% engagement within the first 24 hours.</li>
<li>Brand outcomes are secondary.</li>
</ul>
""",
  "updated":"""
<p><b>Top-line metric: views.</b> Overall reach across the long-form video and its shorts combined. The target is around 1,000,000 views per episode.</p>
<p class="lbl">Primary goals</p>
<ul>
<li><b>Views.</b> Around 1,000,000 per episode, long-form and shorts combined.</li>
<li><b>True engagement rate.</b> Measured on our true-engagement index, tracked across the organic period and then the paid period.</li>
<li><b>Viral hit rate.</b> At least one viral piece per episode on average. Viral means 10,000+ organic views with over 2% engagement within the first 24 hours.</li>
</ul>
<p class="lbl">How we monitor reach</p>
<p>We split organic and paid and watch each separately. Planning split is roughly 20% organic and 80% paid of total views. Organic CPM is far higher because that distribution is expensive; paid CPM is lower. We benchmark CPM off our existing data and share it with Cathy as a reference.</p>
<p class="lbl">Secondary: cost management</p>
<p>Costs are secondary to views. We manage three buckets: production cost, organic and partnership distribution cost, and paid boosting cost. From these we derive cost per episode and cost per impression (CPM). Brand outcomes (branded search lift, new followers, signups) are also tracked as secondary.</p>
"""},

 {"id":"timeline","title":"Timeline",
  "original":"""
<p>A focused UK pilot, a deliberate readout, then staged expansion. Indicative weeks from a late-June 2026 start.</p>
<table><thead><tr><th>Phase</th><th>Timing</th><th>Markets</th></tr></thead><tbody>
<tr><td class="nw">0. Foundation</td><td>Week 1</td><td>Set-up</td></tr>
<tr><td class="nw">1. UK pilot</td><td>Weeks 2-7</td><td>United Kingdom</td></tr>
<tr><td class="nw">2. Pilot readout</td><td>Week 8</td><td>Measure and refine</td></tr>
<tr><td class="nw">3. SEA wave</td><td>Weeks 9-16</td><td>Singapore, Malaysia, Thailand</td></tr>
<tr><td class="nw">4. Europe + Australia</td><td>Weeks 17-24</td><td>Europe, Australia</td></tr>
</tbody></table>
""",
  "userinput":"""
<ul>
<li>No direct input on timing. Reflect the new wave structure.</li>
</ul>
""",
  "updated":"""
<p>Timing carried from the original plan pending your input. The phases now follow the new wave structure.</p>
<table><thead><tr><th>Phase</th><th>Timing</th><th>Markets</th></tr></thead><tbody>
<tr><td class="nw">0. Foundation</td><td>Week 1</td><td>Briefs, rights templates, KPI baseline</td></tr>
<tr><td class="nw">1. UK pilot</td><td>Weeks 2-7</td><td>United Kingdom, one long-form plus ~3 shorts</td></tr>
<tr><td class="nw">2. Pilot readout</td><td>Week 8</td><td>Measure on views, true engagement, viral rate</td></tr>
<tr><td class="nw">3. Wave 2</td><td>Weeks 9-16</td><td>Singapore, Malaysia, Thailand, Vietnam</td></tr>
<tr><td class="nw">4. Wave 3</td><td>Weeks 17-24</td><td>Germany, Poland, Turkey, Australia</td></tr>
<tr><td class="nw">5. Wave 4</td><td>Later</td><td>United States, Mexico and remaining regions</td></tr>
</tbody></table>
"""},

 {"id":"budget","title":"Budget",
  "original":"""
<p>Partner fees benchmarked against 2026 creator rates for micro-tier B2B-niche creators. Figures in US dollars.</p>
<table><thead><tr><th>Market</th><th>Planning rate</th><th>Range</th></tr></thead><tbody>
<tr><td class="nw">United Kingdom</td><td>US$2,000</td><td>US$1,000 - 2,500</td></tr>
<tr><td class="nw">Singapore</td><td>US$1,000</td><td>US$600 - 1,500</td></tr>
<tr><td class="nw">Malaysia</td><td>US$800</td><td>US$300 - 1,000</td></tr>
<tr><td class="nw">Thailand</td><td>US$800</td><td>US$300 - 1,000</td></tr>
<tr><td class="nw">Germany</td><td>US$1,500</td><td>US$1,000 - 2,500</td></tr>
<tr><td class="nw">Poland</td><td>US$1,500</td><td>US$1,000 - 2,000</td></tr>
<tr><td class="nw">Australia</td><td>US$1,000</td><td>US$1,000 - 2,000</td></tr>
<tr><td class="nw">Full Batch 1 (~7 markets)</td><td>~US$8,600</td><td>~US$12,500</td></tr>
</tbody></table>
""",
  "userinput":"""
<ul>
<li>Structure as: production cost + partnership cost (includes distribution) + paid boosting.</li>
</ul>
""",
  "updated":"""
<p>Budget is structured around three cost buckets, matching the cost-management view in the KPIs.</p>
<ul>
<li><b>Production cost.</b> The shoot and editing per episode.</li>
<li><b>Partnership cost (includes distribution).</b> The operator fee plus distribution through the partner's own channels and any co-brand co-publishing. The per-market benchmark below sits here.</li>
<li><b>Paid boosting cost.</b> The paid amplification behind each episode, carrying roughly 80% of total views.</li>
</ul>
<p class="lbl">Partnership cost: benchmarked partner fee per market</p>
<table><thead><tr><th>Market</th><th>Planning rate</th><th>Range</th></tr></thead><tbody>
<tr><td class="nw">United Kingdom</td><td>US$2,000</td><td>US$1,000 - 2,500</td></tr>
<tr><td class="nw">Singapore</td><td>US$1,000</td><td>US$600 - 1,500</td></tr>
<tr><td class="nw">Malaysia</td><td>US$800</td><td>US$300 - 1,000</td></tr>
<tr><td class="nw">Thailand</td><td>US$800</td><td>US$300 - 1,000</td></tr>
<tr><td class="nw">Vietnam</td><td>to benchmark</td><td>SEA band, est. US$500 - 1,200</td></tr>
<tr><td class="nw">Germany</td><td>US$1,500</td><td>US$1,000 - 2,500</td></tr>
<tr><td class="nw">Poland</td><td>US$1,500</td><td>US$1,000 - 2,000</td></tr>
<tr><td class="nw">Turkey</td><td>to benchmark</td><td>Europe-East band, est. US$800 - 1,800</td></tr>
<tr><td class="nw">Australia</td><td>US$1,000</td><td>US$1,000 - 2,000</td></tr>
<tr><td class="nw">United States</td><td>to benchmark</td><td>Western premium, est. US$2,000 - 3,500</td></tr>
<tr><td class="nw">Mexico</td><td>to benchmark</td><td>est. US$600 - 1,500</td></tr>
</tbody></table>
<p class="lbl">Notes</p>
<p>The original ~US$8,600 total covered seven markets and is partnership cost only. New scope (Vietnam, Turkey, United States, Mexico) needs benchmarking, and production plus paid boosting are separate line items still to be priced. Once those land, restate one clean total so the headline figure matches the table (the v2 summary still quotes the old ~US$6,200 / US$9,300).</p>
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
        if s.get("userinput"):
            right = f'<div class="collbl">Your input</div><div class="uinput">{s["userinput"]}</div>'
        else:
            right = f'<div class="collbl">Your input</div><textarea class="inp" data-sid="{s["id"]}" placeholder="drop your notes / direction for this section here"></textarea>'
        if s.get("updated"):
            upd = f'<div class="body">{s["updated"]}</div>'; ucls = "updated has"
        else:
            upd = '<div class="pending">Awaiting your input</div>'; ucls = "updated"
        secs.append(f"""
<section class="sec" id="sec-{s['id']}">
  <div class="sechead"><span class="n">{i:02d}</span><h2>{s['title']}</h2></div>
  <div class="cols">
    <div class="col">
      <div class="collbl">Original &middot; Cathy v2</div>
      <div class="body orig">{s['original']}</div>
    </div>
    <div class="col">{right}</div>
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
  <p class="sub">Original (Cathy v2) on the left, your input captured in the middle, the rebuilt Updated copy below each section.</p>
  <p class="how">Your input is now folded in section by section. Drop more in chat any time and I rebuild. The shorthand to flag: <b>format</b> shorts count (3 vs 4 to 5), and <b>budget</b> still needs production + paid + new-market numbers.</p>
  <div class="meta">Source: Localised Sourcing KOL Series Project Plan_v2.docx &middot; updated 2026-06-16 &middot; <a href="#" onclick="localStorage.removeItem('kolrev_pw');location.reload();return false;">lock device</a></div>
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
.sub{font-size:16px;color:var(--ink2);max-width:780px;margin-bottom:14px}
.how{font-size:13.5px;color:var(--ink3);max-width:780px;background:var(--bg2);border:1px solid var(--line);border-radius:10px;padding:12px 15px}
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
.uinput{font-size:14px;color:var(--ink);background:#fff;border:1px solid var(--line);border-left:2px solid var(--ink);border-radius:8px;padding:16px 18px}
.uinput ul{margin:0;padding-left:18px}
.uinput li{margin-bottom:9px}.uinput li:last-child{margin-bottom:0}
.uinput b{font-weight:620}
textarea.inp{width:100%;min-height:160px;resize:vertical;font:inherit;font-size:14px;line-height:1.55;color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:10px;padding:16px 18px;outline:none;transition:border-color .15s}
textarea.inp:focus{border-color:var(--ink3)}
textarea.inp.filled{border-color:var(--ink);background:#fcfcfd}
.updated{margin-top:18px;border:1px solid var(--line);border-radius:10px;padding:16px 20px;background:#fff}
.updated.has{border-color:var(--ink)}
.updated>.collbl{margin-bottom:12px}
.pending{font-size:13px;color:var(--ink4);font-style:italic}
.foot{margin-top:56px;padding-top:24px;border-top:1px solid var(--line);display:flex;align-items:center;gap:16px}
#copybtn{font:inherit;font-size:14px;font-weight:560;color:#fff;background:var(--ink);border:none;border-radius:8px;padding:11px 20px;cursor:pointer}
#copybtn:hover{background:#000}
#copymsg{font-size:13px;color:var(--ink3)}
.foot .lock{margin-left:auto;font-size:12.5px}
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
  tas.forEach(ta=>{const k='kolrev_input_'+ta.dataset.sid;try{const v=localStorage.getItem(k);if(v){ta.value=v;ta.classList.add('filled');}}catch(_){}ta.addEventListener('input',()=>{try{localStorage.setItem(k,ta.value);}catch(_){}ta.classList.toggle('filled',ta.value.trim().length>0);});});
  const btn=document.getElementById('copybtn'),msg=document.getElementById('copymsg');
  if(btn)btn.addEventListener('click',()=>{
    let out='== KOL series revision input ==\\n';
    tas.forEach(ta=>{const sec=ta.closest('.sec');const t=sec.querySelector('h2').textContent;const n=sec.querySelector('.n').textContent;const v=ta.value.trim();out+='\\n['+n+' '+t+']\\n'+(v?v:'(no change)')+'\\n';});
    if(!tas.length)out+='\\n(all sections already captured in this build)\\n';
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
    with open(os.path.join(HERE, "index.html"), "w") as f:
        f.write(html)
    leak = any(s["original"].strip()[:40] in html for s in SECTIONS)
    print(f"built index.html | {len(html)} chars | password={PASSWORD} | plaintext_leak={leak}")

if __name__ == "__main__":
    main()
