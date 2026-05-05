import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";

const API_URL = "http://127.0.0.1:8000";

const reveal = {
  hidden: {
    opacity: 0,
    y: 70,
    filter: "blur(10px)",
  },
  visible: {
    opacity: 1,
    y: 0,
    filter: "blur(0px)",
    transition: {
      duration: 0.9,
      ease: "easeOut",
    },
  },
};

function App() {
  const [showcase, setShowcase] = useState([]);
  const [form, setForm] = useState({
    name: "",
    artist_name: "",
    email: "",
    project_type: "Animated Loop",
    message: "",
  });

  const [status, setStatus] = useState("");

  useEffect(() => {
    fetch(`${API_URL}/api/showcase`)
      .then((res) => res.json())
      .then((data) => setShowcase(data))
      .catch(() => setShowcase([]));
  }, []);

  const handleChange = (e) => {
    setForm((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const sendContact = async (e) => {
    e.preventDefault();
    setStatus("Sending...");

    try {
      const res = await fetch(`${API_URL}/api/contact`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form),
      });

      const data = await res.json();

      if (data.success) {
        setStatus("Message sent. Let's make something unreal.");
        setForm({
          name: "",
          artist_name: "",
          email: "",
          project_type: "Animated Loop",
          message: "",
        });
      } else {
        setStatus("Something went wrong.");
      }
    } catch {
      setStatus("Backend is not responding.");
    }
  };

  // 🟢 DRAG SCROLL (esto es lo importante)
  const enableDragScroll = (e) => {
    const slider = e.currentTarget;
    slider.dataset.isDown = "true";
    slider.dataset.startX = e.pageX - slider.offsetLeft;
    slider.dataset.scrollLeft = slider.scrollLeft;
  };

  const dragScroll = (e) => {
    const slider = e.currentTarget;
    if (slider.dataset.isDown !== "true") return;

    e.preventDefault();

    const x = e.pageX - slider.offsetLeft;
    const walk = (x - Number(slider.dataset.startX)) * 1.4;

    slider.scrollLeft = Number(slider.dataset.scrollLeft) - walk;
  };

  const stopDragScroll = (e) => {
    e.currentTarget.dataset.isDown = "false";
  };

  return (
    <main className="site">
      <section className="hero">
        <video
          className="hero-video"
          src="/videos/hero-loop.mp4"
          autoPlay
          muted
          loop
          playsInline
        />

        <div className="overlay" />

        <nav className="nav">
          <div className="logo">Lyrics to Frames</div>
          <a href="#contact">Start a Project</a>
        </nav>
<motion.div
  className="hero-content"
  initial={{ opacity: 0, y: 40, filter: "blur(12px)" }}
  animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
  transition={{ duration: 1.1, ease: "easeOut" }}
>
  <p className="eyebrow">Music video animation studio</p>

  <h1>
    Music video animation &{" "}
    <span className="text-accent">Spotify Canvas</span> for artists
  </h1>

  <p className="hero-text">
    Custom animated music videos, Spotify Canvas loops and visual storytelling
    for artists who want their music to be seen, not just heard.
  </p>

  <div className="hero-buttons">
    <a href="#showcase" className="btn primary">
      Watch visuals
    </a>
    <a href="#contact" className="btn secondary">
      Start a project
    </a>
  </div>
</motion.div>
      </section>

      <motion.section
        className="section intro"
        variants={reveal}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, amount: 0.35 }}
      >
       <p>
  I create <span className="text-accent">music video animation</span> and{" "}
  <span className="text-accent">Spotify Canvas loops</span> designed for artists.
  Every frame is built around rhythm, emotion and the visual identity of a song.
</p>
      </motion.section>

      <motion.section
        className="section"
        id="showcase"
        variants={reveal}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, amount: 0.25 }}
      >
        <div className="section-header">
          <p className="eyebrow">Selected visuals</p>
          <h2> Discover <span className="text-accent">a new world</span> behind your songs </h2>
        </div>

        <div
          className="showcase-carousel"
          onMouseDown={enableDragScroll}
          onMouseMove={dragScroll}
          onMouseUp={stopDragScroll}
          onMouseLeave={stopDragScroll}
        >
          {showcase.map((item, index) => (
           <motion.a
  href={item.spotifyUrl}
  target="_blank"
  rel="noreferrer"
  className="visual-card carousel-card"
  key={index}
  initial={{ opacity: 0, y: 40 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, amount: 0.3 }}
  transition={{ duration: 0.7, delay: index * 0.08 }}
>



              <video src={item.video} muted loop playsInline autoPlay />

              <div className="visual-card-info">
                <div>
                  <h3>{item.title}</h3>
                  <p>{item.type}</p>
                </div>

            
              </div>
            </motion.a>
          ))}
        </div>
      </motion.section>

      <motion.section
        className="section process"
        variants={reveal}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, amount: 0.25 }}
      >
        <div className="section-header">
          <p className="eyebrow">The process</p>
          <h2><span className="text-accent">Simple </span>for the artist. <span className="text-accent">Obsessive</span> in the frames.</h2>
        </div>

        <div className="steps">
          {[
            ["01", "Send your track", "You send the song, references and the feeling you want."],
            ["02", "Visual direction", "We define mood, color, symbols and movement style."],
            ["03", "Frame by frame", "I create a visual piece shaped around the rhythm."],
            ["04", "Final delivery", "You receive files ready for socials, shows or release day."],
          ].map(([number, title, text], index) => (
            <motion.div
              key={number}
              initial={{ opacity: 0, y: 35 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.3 }}
              transition={{ duration: 0.65, delay: index * 0.1 }}
            >
              <span>{number}</span>
              <h3>{title}</h3>
              <p>{text}</p>
            </motion.div>
          ))}
        </div>
      </motion.section>

      <motion.section
        className="section contact"
        id="contact"
        variants={reveal}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, amount: 0.25 }}
      >
        <div>
          <p className="eyebrow">Start a project</p>
          <h2>Your music deserves a <span className="text-accent"> visual identity</span>.</h2>
          <p>
            Tell me about the track, the mood and what you want people to feel
            when they see it.
          </p>
        </div>

        <form onSubmit={sendContact}>
          <input
            name="name"
            placeholder="Your name"
            value={form.name}
            onChange={handleChange}
            required
          />

          <input
            name="artist_name"
            placeholder="Artist / band name"
            value={form.artist_name}
            onChange={handleChange}
          />

          <input
            name="email"
            type="email"
            placeholder="Email"
            value={form.email}
            onChange={handleChange}
            required
          />

          <select
            name="project_type"
            value={form.project_type}
            onChange={handleChange}
          >
            <option>Animated Loop</option>
            <option>Music Video</option>
            <option>Live Visuals</option>
            <option>Animated Cover Art</option>
          </select>

          <textarea
            name="message"
            placeholder="Tell me about your song..."
            value={form.message}
            onChange={handleChange}
            required
          />

          <button className="btn primary" type="submit">
            Send project request
          </button>

          {status && <p className="status">{status}</p>}
        </form>
      </motion.section>
    </main>
  );
}

export default App;