"use client";

import { FormEvent, useState } from "react";

const categories = [
  "New small-business website",
  "Existing website redesign",
  "Booking or appointment website",
  "Portfolio or showcase website",
  "Community or membership website",
  "Not sure — help me decide",
  "Other",
];

const services = [
  ["01", "Small business websites", "A professional online home that tells people who you are, what you do and why they should choose you."],
  ["02", "Website redesigns", "Turn an outdated website into something modern, easy to use and built for mobile."],
  ["03", "Bookings & appointments", "Make it easier for customers to enquire, book or arrange an appointment online."],
  ["04", "Portfolios & communities", "Showcase your work or give your community one clear place to find what they need."],
];

const steps = [
  ["1", "Tell us about your business", "Complete our short form and we’ll get in touch for a friendly chat."],
  ["2", "We design and build it", "We create your website, keep you involved and make sure it feels right."],
  ["3", "Review it together", "See everything before launch and tell us about any changes you need."],
  ["4", "Go live with confidence", "Follow our simple setup guidance and we’ll help get your site online."],
];

function LogoMark() {
  return <svg className="logo-mark" viewBox="0 0 92 72" role="img" aria-label="HSW road network logo">
    <path d="M11 10v52M11 36h22M33 10v52M33 18h26c9 0 9 15 0 15H46c-10 0-10 16 0 16h13c9 0 9 13 0 13H33M59 48l8 14 8-25 7 25" fill="none" stroke="currentColor" strokeWidth="9" strokeLinecap="round" strokeLinejoin="round"/>
    <path d="M11 24v7M43 18h8M68 50l3-9" fill="none" stroke="#f6f0e4" strokeWidth="2.4" strokeLinecap="round"/>
    <circle cx="82" cy="28" r="6" fill="#df704e"/>
    <circle cx="64" cy="9" r="2.6" fill="#df704e"/><circle cx="73" cy="9" r="2.6" fill="#efac35"/><circle cx="82" cy="9" r="2.6" fill="currentColor"/>
  </svg>;
}

export default function Home() {
  const [sent, setSent] = useState(false);

  function submitEnquiry(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const form = new FormData(event.currentTarget);
    const subject = encodeURIComponent(`New website enquiry — ${form.get("name")}`);
    const body = encodeURIComponent(`Name: ${form.get("name")}\nEmail: ${form.get("email")}\nPhone: ${form.get("phone")}\nWebsite type: ${form.get("category")}\n\nProject details:\n${form.get("notes")}`);
    setSent(true);
    window.location.href = `mailto:highstreetwebcompany@gmail.com?subject=${subject}&body=${body}`;
  }

  return <main>
    <header className="nav-wrap"><nav className="nav shell" aria-label="Main navigation">
      <a className="brand" href="#top"><LogoMark/><span>High Street<br/>Web Co.</span></a>
      <div className="nav-links"><a href="#services">What we build</a><a href="#process">How it works</a><a href="#about">Why us</a></div>
      <a className="button button-small" href="#enquire">Start a project <span>↗</span></a>
    </nav></header>

    <section className="hero shell" id="top">
      <div className="hero-copy"><p className="eyebrow"><span/> Websites built for local business</p>
        <h1>Your business deserves to look <em>the business.</em></h1>
        <p className="hero-intro">Smart, professional websites for small businesses—built personally, explained simply and designed to help you grow.</p>
        <div className="hero-actions"><a className="button" href="#enquire">Tell us about your business <span>↗</span></a><a className="text-link" href="#process">See how it works ↓</a></div>
        <div className="hero-proof"><div><strong>No monthly</strong><span>hosting fees from us</span></div><div><strong>Built around</strong><span>your business</span></div><div><strong>Friendly support</strong><span>from start to finish</span></div></div>
      </div>
      <div className="hero-art" aria-label="A colourful illustration of independent high-street businesses">
        <div className="sun"/><div className="cloud cloud-one"/><div className="cloud cloud-two"/>
        <div className="shop shop-one"><span className="awning"/><b>BAKERY</b><i/></div><div className="shop shop-two"><span className="awning"/><b>STUDIO</b><i/></div><div className="shop shop-three"><span className="awning"/><b>LOCAL</b><i/></div><div className="pavement"/>
        <div className="browser-card"><span/><span/><span/><strong>Your business,<br/>online.</strong><i/></div>
      </div>
    </section>

    <div className="ticker">LOCAL BUSINESS <i>✦</i> HONEST PRICING <i>✦</i> THOUGHTFUL DESIGN <i>✦</i> PERSONAL SUPPORT <i>✦</i> NO HOSTING FEES FROM US</div>

    <section className="services shell section" id="services">
      <div className="section-heading"><div><p className="eyebrow"><span/> What we build</p><h2>Websites that work as hard as you do.</h2></div><p>Starting from scratch or ready for a fresh look? We’ll create something clear, credible and completely yours.</p></div>
      <div className="service-grid">{services.map(([number,title,copy])=><article key={number}><span>{number}</span><div className="service-icon">{number === "02" ? "↻" : number === "03" ? "□" : number === "04" ? "◎" : "▤"}</div><h3>{title}</h3><p>{copy}</p></article>)}</div>
    </section>

    <section className="no-fees" id="about"><div className="shell no-fees-inner">
      <div className="stamp"><strong>£0</strong><span>monthly hosting<br/>fees from us</span></div>
      <div className="no-fees-copy"><p className="eyebrow light"><span/> Keep more of what you earn</p><h2>A brilliant website without ongoing hosting fees.</h2><p>Small businesses deserve a professional website without expensive monthly hosting charges. You pay for the design and build, then we give you simple instructions to get everything set up and live.</p><p>Your only separate ongoing cost is your chosen domain name, which normally costs a small amount each year.</p><div className="promise"><b>✓</b><span><strong>No confusing packages. No unnecessary monthly bills.</strong><br/>Just a modern website and friendly support when you need it.</span></div></div>
    </div></section>

    <section className="process shell section" id="process"><div className="center-heading"><p className="eyebrow"><span/> Nice and straightforward</p><h2>From first chat to live website.</h2><p>No jargon and no disappearing acts. You’ll always know what’s happening next.</p></div><div className="steps">{steps.map(([number,title,copy])=><article key={number}><b>{number}</b><h3>{title}</h3><p>{copy}</p></article>)}</div></section>

    <section className="enquiry-section" id="enquire"><div className="shell enquiry-grid">
      <div className="enquiry-copy"><p className="eyebrow light"><span/> Let’s build something good</p><h2>Tell us what you have in mind.</h2><p>You don’t need a detailed brief or technical knowledge. Tell us about your business and what you’d like your website to do—we’ll help with the rest.</p><a href="mailto:highstreetwebcompany@gmail.com">highstreetwebcompany@gmail.com</a><div className="local-note"><b>⌂</b><span><strong>Proud to support small business</strong><br/>Personal service, honest advice and websites made with care.</span></div></div>
      <form className="enquiry-form" onSubmit={submitEnquiry}>
        <div className="field-row"><label>Your name<input name="name" autoComplete="name" placeholder="e.g. Sarah Jones" required/></label><label>Email address<input name="email" type="email" autoComplete="email" placeholder="you@business.co.uk" required/></label></div>
        <label>Phone number<input name="phone" type="tel" autoComplete="tel" placeholder="Your preferred contact number" required/></label>
        <label>What sort of website do you need?<select name="category" defaultValue="" required><option value="" disabled>Choose the closest option</option>{categories.map(category=><option key={category}>{category}</option>)}</select></label>
        <label>Tell us a little about your project<textarea name="notes" rows={5} placeholder="What does your business do? What would you like the website to help you achieve?" required/></label>
        <button className="button form-button" type="submit">Send my enquiry <span>↗</span></button><p className="form-note">By sending this form, you agree that we may contact you about your enquiry. No spam, ever.</p>{sent&&<p className="sent">Your email app should now open with your enquiry ready to send.</p>}
      </form>
    </div></section>

    <footer><div className="shell footer-grid"><div className="brand footer-brand"><LogoMark/><span>High Street<br/>Web Co.</span></div><p>Websites built for local business.</p><a href="mailto:highstreetwebcompany@gmail.com">highstreetwebcompany@gmail.com</a></div><div className="shell footer-bottom"><span>© {new Date().getFullYear()} High Street Web Co.</span><span>Supporting small businesses, one website at a time.</span></div></footer>
  </main>;
}
