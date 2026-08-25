#!/usr/bin/env python3
"""Service, FAQ and legal pages.  python3 build_services.py"""
import io, json
from build_pages import page, head_block, cta, SITE

OUT = []
def emit(slug, **kw):
    io.open(slug, "w", encoding="utf-8").write(page(slug, **kw)); OUT.append(slug)

UPDATED = "22 August 2026"

# ─────────────────────────────────────────────── SERVICES HUB
emit("services.html",
  title="Services | Golden Hour Wellness Colorado",
  desc="Trauma and EMDR therapy, anxiety and depression, substance use counseling, couples work, and a virtual therapy group for Colorado mothers.",
  body=head_block("How we help", "Specialized care, without the clinical chill.",
    "Every clinician here brings a different lane of expertise. We&rsquo;ll help you find the right fit on your first call, even if that fit turns out to be somewhere else.") + '''
<section class="section">
  <div class="wrap">
    <div class="cards">
      <a class="card" href="trauma-emdr.html"><h3>Trauma &amp; EMDR</h3><p>Eye Movement Desensitization and Reprocessing alongside other trauma-focused approaches.</p><span class="more">Learn more &rarr;</span></a>
      <a class="card" href="anxiety-depression.html"><h3>Anxiety &amp; Depression</h3><p>Solution-oriented, CBT-informed work, plus practical tools you can actually use.</p><span class="more">Learn more &rarr;</span></a>
      <a class="card" href="substance-use.html"><h3>Substance Use &amp; Recovery</h3><p>Licensed addiction counseling for substance use disorders, or feeling stuck and disconnected.</p><span class="more">Learn more &rarr;</span></a>
      <a class="card" href="couples-therapy.html"><h3>Couples &amp; Relationships</h3><p>Family stress, work stress, and the big pivots that change how you relate to each other.</p><span class="more">Learn more &rarr;</span></a>
      <a class="card" href="mamas-golden-hour.html"><h3>Mama&rsquo;s Golden Hour</h3><p>A six-week virtual therapy group for Colorado mothers. Next cohort begins 7 October.</p><span class="more">Learn more &rarr;</span></a>
    </div>
    <div class="callout" style="margin-top:2.5rem; max-width:44rem">
      <p><strong>Individual therapy</strong> is the default format for everything above except the group. Sessions run 50 minutes, in person or by telehealth anywhere in Colorado.</p>
    </div>
  </div>
</section>''' + cta())

# ─────────────────────────────────────────────── SERVICE PAGES
def service(slug, name, title, desc, lede, paras, good_fit, practical, who):
    ld = {"@context":"https://schema.org","@type":"MedicalTherapy","name":name,
          "url":f"{SITE}/{slug}",
          "provider":{"@type":"MedicalBusiness","name":"Golden Hour Wellness Colorado, LLC",
                      "areaServed":{"@type":"State","name":"Colorado"}}}
    fit = "".join(f"<li>{x}</li>" for x in good_fit)
    body = head_block("Services", title, lede) + f'''
<section class="section">
  <div class="wrap prose">
    {"".join(f"<p>{p}</p>" for p in paras)}

    <h2>This may be a good fit if</h2>
    <ul>{fit}</ul>

    <h2>Practical details</h2>
    {practical}

    <div class="callout">
      <p><strong>Who you&rsquo;d see:</strong> {who}</p>
    </div>
  </div>
</section>''' + cta()
    emit(slug, title=f"{title} | Golden Hour Wellness Colorado", desc=desc, body=body,
         active="services.html",
         extra_head=f'<script type="application/ld+json">{json.dumps(ld)}</script>')

STD = '''<table>
      <tr><th>Format</th><td>Individual, 50 minutes</td></tr>
      <tr><th>Where</th><td>In person or telehealth, anywhere in Colorado</td></tr>
      <tr><th>Insurance</th><td>In-network with Aetna, United Healthcare and Cigna</td></tr>
      <tr><th>First step</th><td>A free 15-minute consultation</td></tr>
    </table>'''

service("trauma-emdr.html", "EMDR Therapy", "Trauma &amp; EMDR Therapy",
  "EMDR and trauma-focused therapy in Colorado. Eye Movement Desensitization and Reprocessing with a Licensed Professional Counselor, in person or by telehealth.",
  "Eye Movement Desensitization and Reprocessing alongside other trauma-focused approaches, in person or via telehealth.",
  ["Trauma doesn&rsquo;t only live in memory. It shows up in how your body reacts, how you sleep, what you avoid, and how quickly you move from calm to overwhelmed. EMDR works with that directly rather than asking you to talk your way through it.",
   "The goal isn&rsquo;t to erase what happened. It&rsquo;s to change your relationship to it, so the memory stops setting the terms of your present. Most people find they can hold more, react less, and recognise themselves again.",
   "Shayla uses EMDR among other trauma-focused approaches, chosen to fit what you bring rather than applied from a template. You&rsquo;ll never be pushed to revisit something before you&rsquo;re ready."],
  ["Something from your past still shapes how you react today",
   "You feel activated or shut down without always knowing why",
   "Talk therapy has helped, but only to a point",
   "You&rsquo;re carrying a single event, or years of accumulated stress",
   "You want structure rather than open-ended conversation"],
  STD, 'Shayla Martinez-O&rsquo;Brien, LPC, LAC. <a href="shayla.html">Read her profile</a>.')

service("anxiety-depression.html", "Cognitive Behavioral Therapy", "Anxiety &amp; Depression",
  "Therapy for anxiety and depression in Colorado. Solution-oriented, CBT-informed counseling with licensed clinicians, in person or by telehealth.",
  "Solution-oriented, CBT-informed work on how mood, thoughts and behavior shape one another, plus tools you can actually use.",
  ["Anxiety and depression are good at convincing you that this is simply how you are. They aren&rsquo;t, and the pattern is more changeable than it feels from inside it.",
   "The work looks at how mood, thought and behaviour feed one another, then interrupts that loop somewhere practical. Often the first useful change is small and unglamorous, like what happens in the first hour of your day.",
   "You&rsquo;ll leave sessions with something to try, not just something to think about. And we&rsquo;ll keep an honest eye on whether it&rsquo;s working."],
  ["Worry runs constantly in the background",
   "You&rsquo;ve lost interest in things that used to matter",
   "Sleep, appetite or focus have shifted",
   "You&rsquo;re functioning, but it&rsquo;s costing more than it should",
   "You want practical tools alongside understanding"],
  STD, 'Shayla Martinez-O&rsquo;Brien or Chrissie Flynn-Weirich. <a href="team.html">Meet the team</a>.')

service("substance-use.html", "Addiction Counseling", "Substance Use &amp; Recovery",
  "Licensed addiction counseling in Colorado for substance use disorders. Non-judgmental, strengths-based support in person or by telehealth.",
  "Licensed addiction counseling for people living with substance use disorders, or anyone feeling stuck and disconnected from themselves.",
  ["You don&rsquo;t need a label or a rock-bottom story to start here. Plenty of people arrive simply knowing something has taken up more room than they want it to.",
   "The work is strengths-based. We&rsquo;ll identify what&rsquo;s already working, name honestly what isn&rsquo;t, and set goals that match your own vision of your best self rather than someone else&rsquo;s.",
   "Both clinicians here hold Colorado addiction counseling licences, which is less common than it sounds. It means substance use is treated as core clinical work, not as a referral."],
  ["Substance use has become larger than you intended",
   "You feel stuck, or disconnected from yourself and others",
   "You&rsquo;ve tried to change on your own and it hasn&rsquo;t held",
   "You want support that isn&rsquo;t shaming or scripted",
   "You&rsquo;re navigating recovery alongside trauma or anxiety"],
  STD, 'Chrissie Flynn-Weirich, LAC, or Shayla Martinez-O&rsquo;Brien, LPC, LAC.')

service("couples-therapy.html", "Couples Therapy", "Couples &amp; Relationships",
  "Couples and relationship counseling in Colorado. Support for communication, family and work stress, and major life transitions.",
  "Family stress, work stress, and the big pivots. Navigating change with more clarity and a stronger sense of purpose.",
  ["Most couples don&rsquo;t arrive because of one argument. They arrive because a pattern has set in, and the same conversation keeps happening in slightly different clothes.",
   "Sessions focus on what each of you is actually asking for underneath the disagreement, and on building a way to say it that the other person can hear.",
   "This is also useful during transitions that aren&rsquo;t anyone&rsquo;s fault. A new baby, a career change, a move, an illness, or a shift in what you each need."],
  ["The same argument keeps recurring",
   "A transition has changed how you relate to each other",
   "One or both of you has stopped raising things",
   "You want to communicate differently, not just less often",
   "You&rsquo;re deciding whether to continue and want support either way"],
  STD, 'Shayla Martinez-O&rsquo;Brien or Chrissie Flynn-Weirich.')

# ─────────────────────────────────────────────── MAMA'S GOLDEN HOUR
group_ld = {"@context":"https://schema.org","@type":"Event",
  "name":"Mama's Golden Hour Therapy Group","eventAttendanceMode":"https://schema.org/OnlineEventAttendanceMode",
  "eventStatus":"https://schema.org/EventScheduled","startDate":"2026-10-07T18:00:00-06:00",
  "location":{"@type":"VirtualLocation","url":f"{SITE}/mamas-golden-hour.html"},
  "organizer":{"@type":"MedicalBusiness","name":"Golden Hour Wellness Colorado, LLC"},
  "description":"A six-week virtual therapy group for Colorado mothers covering fertility, pregnancy and birth, postpartum and all stages of parenting.",
  "offers":{"@type":"Offer","price":"150","priceCurrency":"USD","availability":"https://schema.org/InStock","url":f"{SITE}/mamas-golden-hour.html"}}

emit("mamas-golden-hour.html",
  title="Mama&rsquo;s Golden Hour | Therapy Group for Colorado Moms",
  desc="A six-week virtual therapy group for Colorado mothers, covering fertility, pregnancy, postpartum and parenting. Next cohort begins 7 October.",
  active="services.html",
  extra_head=f'<script type="application/ld+json">{json.dumps(group_ld)}</script>',
  body=head_block("Group therapy", "Mama&rsquo;s Golden Hour",
    "A six-week virtual therapy group for mothers across Colorado, co-facilitated by Shayla and Ashley.") + '''
<section class="section">
  <div class="wrap prose">
    <p>Motherhood asks a great deal and rarely leaves room to talk about it honestly. This group is that room: a small, virtual space with other Colorado mothers and two licensed clinicians.</p>

    <p>We cover the whole arc rather than one stage of it. Fertility, pregnancy and birth, postpartum, and every stage of parenting after that. Wherever you are in it, you&rsquo;re welcome.</p>

    <h2>Next cohort</h2>
    <table>
      <tr><th>Starts</th><td>Wednesday 7 October 2026</td></tr>
      <tr><th>Time</th><td>6:00pm Mountain Time</td></tr>
      <tr><th>Runs for</th><td>6 weeks</td></tr>
      <tr><th>Where</th><td>Virtually, via Zoom</td></tr>
      <tr><th>Cost</th><td>$25 per session, or $150 for the full six weeks</td></tr>
      <tr><th>Open to</th><td>Mothers anywhere in Colorado</td></tr>
    </table>

    <div class="callout warn">
      <p><strong>Insurance is not accepted for the group.</strong> Group sessions are self-pay only. Insurance does apply to individual therapy, where we&rsquo;re in-network with Aetna, United Healthcare and Cigna.</p>
    </div>

    <h2>What it covers</h2>
    <ul>
      <li>Fertility, and the particular loneliness of that season</li>
      <li>Pregnancy and birth, including births that didn&rsquo;t go to plan</li>
      <li>Postpartum, and the gap between how you expected to feel and how you do</li>
      <li>All stages of parenting, from newborn nights to older children</li>
      <li>Identity, resentment, guilt, and the things that feel unsayable elsewhere</li>
    </ul>

    <h2>Who facilitates</h2>
    <p>The group is co-facilitated by <a href="shayla.html">Shayla Martinez-O&rsquo;Brien</a>, LPC, LAC, and <a href="ashley.html">Ashley LeRossignol</a>, LPC.</p>

    <h2>Joining</h2>
    <p>Every member has a short consultation first, so we can make sure the group is a good fit before you commit. Call or text <a href="tel:+13037369822">(303)&nbsp;736-9822</a>, or <a href="contact.html">send a message</a>.</p>
  </div>
</section>

<section class="section" style="background:var(--sand); text-align:center">
  <div class="wrap">
    <h2>Join the October cohort</h2>
    <p class="lede" style="margin-inline:auto">Six weeks, starting Wednesday 7 October at 6pm MT. Consultation first, always.</p>
    <div style="display:flex; gap:.7rem; justify-content:center; flex-wrap:wrap; margin-top:1.75rem">
      <a class="btn btn-primary" href="index.html#book">Book a consultation</a>
      <a class="btn btn-outline" href="tel:+13037369822">Call or text (303) 736-9822</a>
    </div>
  </div>
</section>''')

print("wrote:", len(OUT)); [print("  ", o) for o in OUT]
