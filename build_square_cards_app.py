import os

with open('images_data.js', 'r', encoding='utf-8') as f:
    images_code = f.read()

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>Happy Birthday, Mom! ✨ Aesthetic Memory Scrapbook</title>
  <meta name="description" content="A handcrafted aesthetic scrapbook for Mom: opening envelope, single-page confined square cards board without scroll, and dedicated story pages." />

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400..700&family=Cormorant+Garamond:ital,wght@0,500;0,700;1,500;1,700&family=DM+Sans:ital,opsz,wght@0,9..40,400..700;1,9..40,400&family=Homemade+Apple&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,700;1,6..72,400&family=Playfair+Display:ital,wght@0,600;0,800;1,600&family=Special+Elite&display=swap" rel="stylesheet">

  <style>
    /* ═══════════════════════════════════════════════════════════
       1. GLOBAL RESET & EXACT COLOR TOKENS
       ═══════════════════════════════════════════════════════════ */
    :root {
      --bg-desk: #ECE4D8;
      --paper-cream: #FCF9F2;
      --paper-warm: #FAF4EB;
      --paper-kraft: #D9C3AA;
      --paper-news: #E8DEC8;
      --spotify-brick: #6B231F;
      --spotify-dark: #121212;
      --spotify-green: #1DB954;
      --rose-pink: #E8A0A8;
      --blush: #F9D8D6;
      --plum-ink: #3D2633;
      --plum-soft: #634657;
      --gold-foil: #D4AF37;
      --heart-red: #E63946;

      --font-retro: 'Special Elite', 'Courier New', monospace;
      --font-hand: 'Caveat', cursive;
      --font-script: 'Homemade Apple', cursive;
      --font-serif: 'Playfair Display', Georgia, serif;
      --font-editorial: 'Newsreader', Georgia, serif;
      --font-headline: 'Cormorant Garamond', Georgia, serif;
      --font-sans: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;

      --shadow-polaroid: 0 8px 18px -3px rgba(61, 38, 51, 0.18), 0 2px 6px -1px rgba(61, 38, 51, 0.1);
      --shadow-card: 0 6px 16px -3px rgba(61, 38, 51, 0.15), 0 2px 5px rgba(61, 38, 51, 0.08);
      --shadow-sticker: 0 3px 8px rgba(61, 38, 51, 0.15);
      --shadow-hover: 0 16px 30px -4px rgba(61, 38, 51, 0.28);
      --ease-smooth: cubic-bezier(0.22, 1, 0.36, 1);
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
      -webkit-user-drag: none;
    }

    html, body {
      width: 100vw;
      height: 100vh;
      max-width: 100vw;
      max-height: 100vh;
      overflow: hidden;
      background-color: var(--bg-desk);
      color: var(--plum-ink);
      font-family: var(--font-sans);
      position: relative;
    }

    /* Paper & film grain overlay */
    .film-grain {
      position: fixed;
      inset: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 1000;
      opacity: 0.035;
      mix-blend-mode: multiply;
    }

    /* Confetti Canvas */
    #confettiCanvas {
      position: fixed;
      inset: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 3500;
    }

    /* ═══════════════════════════════════════════════════════════
       VIEW 1: OPENING PAGE (#coverScreen)
       ═══════════════════════════════════════════════════════════ */
    #coverScreen {
      position: fixed;
      inset: 0;
      width: 100vw;
      height: 100vh;
      background: radial-gradient(circle at center, #FFFBF5 0%, #EFE5D5 65%, #DFD2BF 100%);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 2000;
      transition: opacity 0.65s var(--ease-smooth), transform 0.65s var(--ease-smooth);
      cursor: pointer;
    }

    #coverScreen.opened {
      opacity: 0;
      transform: scale(1.06);
      pointer-events: none;
      visibility: hidden;
    }

    .cover-card-box {
      width: min(90vw, 420px);
      background: #FFFDF9;
      border: 1px solid rgba(201, 166, 107, 0.4);
      border-radius: 18px;
      padding: 34px 26px;
      box-shadow: 0 25px 50px -12px rgba(61, 38, 51, 0.25), 0 0 0 1px rgba(255, 255, 255, 0.8) inset;
      text-align: center;
      position: relative;
      animation: floatCover 4s ease-in-out infinite alternate;
    }

    @keyframes floatCover {
      0% { transform: translateY(0) rotate(-0.5deg); }
      100% { transform: translateY(-7px) rotate(0.8deg); }
    }

    .cover-tape-top {
      position: absolute;
      top: -14px;
      left: 50%;
      transform: translateX(-50%) rotate(1deg);
      width: 110px;
      height: 24px;
      background: rgba(232, 160, 168, 0.7);
      border-left: 2px dashed rgba(255,255,255,0.7);
      border-right: 2px dashed rgba(255,255,255,0.7);
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }

    .cover-eyebrow {
      font-family: var(--font-retro);
      font-size: 0.78rem;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: #9E748B;
      margin-bottom: 10px;
    }

    .cover-title {
      font-family: var(--font-headline);
      font-size: clamp(2.2rem, 4.5vw, 3rem);
      font-style: italic;
      line-height: 1.15;
      color: var(--plum-ink);
      margin-bottom: 8px;
    }

    .cover-subtitle {
      font-family: var(--font-hand);
      font-size: 1.45rem;
      color: var(--plum-soft);
      line-height: 1.35;
      margin-bottom: 22px;
    }

    .cover-seal-btn {
      width: 72px;
      height: 72px;
      border-radius: 50%;
      margin: 0 auto 14px auto;
      background: radial-gradient(circle at 35% 35%, #F44336 0%, #C62828 55%, #8E0000 100%);
      box-shadow: 0 8px 18px rgba(180, 20, 20, 0.4), inset 0 2px 5px rgba(255, 255, 255, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #FFF;
      font-size: 1.9rem;
      border: 3px solid rgba(255, 215, 0, 0.6);
      cursor: pointer;
      animation: pulseSeal 2s infinite ease-in-out;
    }

    @keyframes pulseSeal {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.08); box-shadow: 0 12px 26px rgba(180, 20, 20, 0.55), 0 0 18px rgba(255, 215, 0, 0.7); }
    }

    .cover-prompt {
      font-family: var(--font-hand);
      font-size: 1.2rem;
      color: var(--plum-soft);
      font-weight: 700;
    }

    /* ═══════════════════════════════════════════════════════════
       VIEW 2: CONFINED CARDS BOARD (ALL CARDS ARE UNIQUE SQUARES!)
       ═══════════════════════════════════════════════════════════ */
    #cardsBoard {
      width: 100vw;
      height: 100vh;
      max-width: 100vw;
      max-height: 100vh;
      overflow: hidden;
      position: fixed;
      inset: 0;
      background-color: var(--bg-desk);
      background-image: 
        radial-gradient(rgba(61, 38, 51, 0.05) 1px, transparent 1px),
        linear-gradient(to right, rgba(201, 166, 107, 0.04) 1px, transparent 1px);
      background-size: 20px 20px, 100px 100px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      z-index: 10;
    }

    /* Top Action Bar */
    .top-action-bar {
      width: 100%;
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 14px;
      padding: 6px 16px;
      position: relative;
      z-index: 50;
      flex-shrink: 0;
    }

    .btn-top-pill {
      background: rgba(255, 253, 249, 0.94);
      border: 1px solid rgba(201, 166, 107, 0.4);
      backdrop-filter: blur(8px);
      padding: 6px 18px;
      border-radius: 9999px;
      font-family: var(--font-hand);
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--plum-ink);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 7px;
      box-shadow: 0 3px 8px rgba(61, 38, 51, 0.08);
      transition: all 0.2s ease;
    }

    .btn-top-pill:hover {
      background: #FFF;
      transform: translateY(-2px);
      box-shadow: 0 5px 12px rgba(61, 38, 51, 0.14);
      color: var(--spotify-brick);
    }

    .btn-top-pill .vinyl-dot {
      width: 13px;
      height: 13px;
      border-radius: 50%;
      background: #111;
      border: 2px solid var(--gold-foil);
      display: inline-block;
    }

    .btn-top-pill.playing .vinyl-dot {
      animation: spinVinyl 2s linear infinite;
    }

    @keyframes spinVinyl {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    /* Background Newspaper Scraps */
    .bg-newspaper-scrap {
      position: absolute;
      background: var(--paper-news);
      border: 1px solid rgba(0, 0, 0, 0.08);
      font-family: var(--font-retro);
      font-size: 0.62rem;
      line-height: 1.15;
      color: rgba(61, 38, 51, 0.55);
      padding: 8px;
      pointer-events: none;
      z-index: 1;
      opacity: 0.65;
    }

    .scrap-tl {
      top: 10px;
      left: 12px;
      width: clamp(140px, 15vw, 200px);
      transform: rotate(-5deg);
    }

    .scrap-br {
      bottom: 10px;
      right: 14px;
      width: clamp(150px, 16vw, 220px);
      transform: rotate(3deg);
    }

    /* ═══════════════════════════════════════════════════════════
       THE SQUARE CARDS GRID (4 COLUMNS × 2 ROWS • ZERO SCROLL)
       ═══════════════════════════════════════════════════════════ */
    .square-board-wrapper {
      flex: 1;
      width: 100%;
      height: calc(100vh - 52px);
      max-height: calc(100vh - 52px);
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      padding: 6px 24px 16px 24px;
      box-sizing: border-box;
    }

    .square-cards-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      grid-template-rows: repeat(2, 1fr);
      gap: clamp(14px, 2.4vh, 26px) clamp(16px, 2.5vw, 32px);
      align-items: center;
      justify-items: center;
      max-width: 1040px;
      width: 100%;
      margin: auto;
      z-index: 10;
    }

    /* COMMON SQUARE CARD BASE - STRICT SQUARE ASPECT RATIO */
    .square-card {
      width: clamp(160px, 23.5vh, 225px);
      height: clamp(160px, 23.5vh, 225px);
      aspect-ratio: 1 / 1;
      border-radius: 8px;
      box-shadow: var(--shadow-card);
      cursor: pointer;
      position: relative;
      overflow: hidden;
      transition: transform 0.24s var(--ease-smooth), box-shadow 0.24s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: clamp(9px, 1.3vh, 14px);
      box-sizing: border-box;
      z-index: 10;
    }

    .square-card:hover {
      transform: translateY(-6px) scale(1.05) rotate(0deg) !important;
      box-shadow: var(--shadow-hover) !important;
      z-index: 35 !important;
    }

    /* ── SQUARE CARD 1: BABY POLAROID ── */
    .sq-card-polaroid-baby {
      background: #FFFFFF;
      transform: rotate(-2deg);
      border: 1px solid rgba(0,0,0,0.06);
    }

    .sq-polaroid-tape {
      position: absolute;
      top: -6px;
      left: 50%;
      transform: translateX(-50%);
      width: 55px;
      height: 15px;
      background: rgba(255, 255, 255, 0.8);
      box-shadow: 0 1px 3px rgba(0,0,0,0.12);
      z-index: 5;
    }

    .sq-photo-frame {
      width: 100%;
      flex: 1;
      min-height: 0;
      background: #111;
      overflow: hidden;
      border-radius: 2px;
      position: relative;
    }

    .sq-photo-frame img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .sq-card-polaroid-baby .sq-photo-frame img {
      object-position: center 2%;
    }

    .sq-card-polaroid-family .sq-photo-frame img {
      object-position: center 70%;
    }

    .sq-polaroid-caption {
      margin-top: 6px;
      font-family: var(--font-hand);
      font-size: clamp(1.05rem, 1.5vh, 1.25rem);
      color: var(--plum-ink);
      text-align: center;
      font-weight: 700;
      line-height: 1.1;
    }

    /* ── SQUARE CARD 2: VINTAGE TORN QUOTE ── */
    .sq-card-quote {
      background: var(--paper-warm);
      transform: rotate(1.5deg);
      justify-content: center;
      text-align: center;
      border: 1px solid rgba(201, 166, 107, 0.25);
      padding: clamp(12px, 1.8vh, 18px);
    }

    .sq-torn-corner {
      position: absolute;
      top: 0;
      left: 0;
      width: 32px;
      height: 32px;
      background: var(--paper-news);
      clip-path: polygon(0 0, 100% 0, 0 100%);
      font-family: var(--font-retro);
      font-size: 0.38rem;
      line-height: 0.8;
      overflow: hidden;
      padding: 2px;
      color: rgba(61, 38, 51, 0.5);
    }

    .sq-quote-text {
      font-family: var(--font-editorial);
      font-size: clamp(0.9rem, 1.45vh, 1.12rem);
      line-height: 1.35;
      color: var(--plum-ink);
      font-style: italic;
    }

    .sq-quote-author {
      font-family: var(--font-hand);
      font-size: 1.05rem;
      color: var(--plum-soft);
      margin-top: 6px;
    }

    /* ── SQUARE CARD 3: SPOTIFY BRICK RED ── */
    .sq-card-spotify-red {
      background: var(--spotify-brick);
      color: #FFF;
      transform: rotate(-1deg);
    }

    .sq-spotify-header {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .sq-album-thumb {
      width: clamp(30px, 4.2vh, 40px);
      height: clamp(30px, 4.2vh, 40px);
      border-radius: 3px;
      background: #2A0E0C;
      overflow: hidden;
      flex-shrink: 0;
    }

    .sq-track-title {
      font-size: clamp(0.74rem, 1.05vw, 0.86rem);
      font-weight: 700;
      color: #FFF;
      line-height: 1.15;
    }

    .sq-track-artist {
      font-size: 0.64rem;
      color: rgba(255,255,255,0.7);
    }

    .sq-spotify-lyrics {
      font-family: var(--font-editorial);
      font-size: clamp(0.85rem, 1.3vh, 1.05rem);
      font-style: italic;
      line-height: 1.3;
      color: #FFFDF9;
      margin: auto 0;
    }

    .sq-spotify-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid rgba(255, 255, 255, 0.18);
      padding-top: 4px;
    }

    /* ── SQUARE CARD 4: UNPAID THERAPIST KRAFT ── */
    .sq-card-therapist {
      background: var(--paper-kraft);
      transform: rotate(2deg);
      text-align: center;
      align-items: center;
      border: 1.5px dashed rgba(61, 38, 51, 0.28);
    }

    .sq-therapist-title {
      font-family: var(--font-hand);
      font-size: clamp(1.1rem, 1.6vh, 1.35rem);
      font-weight: 700;
      color: #2F1E29;
      line-height: 1.15;
    }

    .sq-therapist-heart {
      width: clamp(32px, 4.6vh, 44px);
      height: clamp(32px, 4.6vh, 44px);
      margin: 2px 0;
      animation: heartbeat 2s infinite ease-in-out;
    }

    @keyframes heartbeat {
      0%, 100% { transform: scale(1); }
      15% { transform: scale(1.18); }
      30% { transform: scale(1); }
      45% { transform: scale(1.12); }
    }

    .sq-therapist-sub {
      font-family: var(--font-hand);
      font-size: 0.95rem;
      color: #523546;
      line-height: 1.1;
    }

    /* ── SQUARE CARD 5: BEST-TEA SQUARE ── */
    .sq-card-best-tea {
      background: #FFFFFF;
      transform: rotate(1.2deg);
      text-align: center;
      align-items: center;
    }

    .sq-best-tea-title {
      font-family: var(--font-hand);
      font-size: clamp(1.05rem, 1.5vh, 1.25rem);
      font-weight: 800;
      color: var(--plum-ink);
      line-height: 1.1;
    }

    /* ── SQUARE CARD 6: TEDDY BEAR BIRTHDAY CAKE SQUARE ── */
    .sq-card-cake {
      background: #FFFFFF;
      transform: rotate(-1.5deg);
      align-items: center;
      justify-content: center;
      text-align: center;
    }

    .cake-flame-svg {
      transform-origin: 75px 12px;
      animation: flameWiggle 1.4s ease-in-out infinite alternate;
      cursor: pointer;
    }

    @keyframes flameWiggle {
      0% { transform: scale(1) rotate(-3deg); }
      100% { transform: scale(1.12) rotate(3deg); }
    }

    .cake-flame-svg.blown {
      opacity: 0;
      transform: scale(0.2) translateY(-8px);
    }

    .sq-cake-prompt {
      font-family: var(--font-hand);
      font-size: 0.95rem;
      color: #9E748B;
      font-weight: 700;
      margin-top: 3px;
    }

    /* ── SQUARE CARD 7: SPOTIFY WHITE SQUARE ── */
    .sq-card-spotify-white {
      background: #FFFFFF;
      transform: rotate(1.8deg);
    }

    .sq-white-quote {
      font-family: var(--font-headline);
      font-size: clamp(0.92rem, 1.38vh, 1.15rem);
      font-weight: 700;
      color: #1A1A1A;
      line-height: 1.25;
      margin: auto 0;
    }

    .sq-pink-line {
      display: block;
      width: 100%;
      height: 6px;
      background: rgba(232, 160, 168, 0.55);
      border-radius: 3px;
      margin-top: 3px;
    }

    /* ── SQUARE CARD 8: FAMILY MILESTONE POLAROID ── */
    .sq-card-polaroid-family {
      background: #FFFFFF;
      transform: rotate(-2deg);
      border: 1px solid rgba(0,0,0,0.06);
    }

    .sq-family-tape {
      position: absolute;
      top: -5px;
      left: 50%;
      transform: translateX(-50%);
      width: 55px;
      height: 14px;
      background: linear-gradient(135deg, #ECC47E 0%, #D4A95B 40%, #F5E0A8 80%, #C99738 100%);
      box-shadow: 0 1px 3px rgba(0,0,0,0.12);
      z-index: 5;
    }

    .sq-bubble-tag {
      position: absolute;
      top: 5px;
      right: 5px;
      background: rgba(255, 255, 255, 0.95);
      padding: 3px 6px;
      border-radius: 4px;
      font-family: var(--font-hand);
      font-size: 0.72rem;
      line-height: 1;
      color: #2F1E29;
      box-shadow: 0 1px 4px rgba(0,0,0,0.15);
      z-index: 6;
      max-width: 100px;
    }

    /* ═══════════════════════════════════════════════════════════
       STICKERS & DOODLES (AROUND THE SQUARES)
       ═══════════════════════════════════════════════════════════ */
    .sticker-floating {
      position: absolute;
      pointer-events: auto;
      z-index: 25;
      filter: drop-shadow(var(--shadow-sticker));
      transition: transform 0.2s ease;
      cursor: pointer;
    }

    .sticker-floating:hover {
      transform: scale(1.12) rotate(var(--hover-rot, 4deg));
    }

    .sticker-lungs {
      top: 6vh;
      right: 3vw;
      width: clamp(65px, 7vw, 90px);
      transform: rotate(4deg);
      --hover-rot: -2deg;
    }

    .sticker-huggers {
      top: 8vh;
      left: 3vw;
      width: clamp(50px, 5.5vw, 70px);
      transform: rotate(-5deg);
      --hover-rot: 3deg;
    }

    .sticker-hbd-banner {
      bottom: 5vh;
      left: 3vw;
      width: clamp(80px, 9vw, 115px);
      transform: rotate(10deg);
      --hover-rot: 6deg;
    }

    .sticker-rose {
      bottom: 4vh;
      right: 3vw;
      width: clamp(80px, 9vw, 115px);
      transform: rotate(-3deg);
    }

    .sticker-puzzle {
      top: 50%;
      right: 1vw;
      width: clamp(55px, 6vw, 75px);
      transform: translateY(-50%) rotate(5deg);
    }

    /* ═══════════════════════════════════════════════════════════
       VIEW 3: INDEPENDENT DEDICATED STORY PAGES VIEW
       ═══════════════════════════════════════════════════════════ */
    #detailPageView {
      display: none;
      position: fixed;
      inset: 0;
      width: 100vw;
      height: 100vh;
      background-color: var(--bg-desk);
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      z-index: 100;
      padding: 24px 20px 60px 20px;
    }

    .page-nav-bar {
      max-width: 920px;
      margin: 0 auto 20px auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px dashed rgba(201, 166, 107, 0.4);
      padding-bottom: 14px;
      flex-wrap: wrap;
      gap: 10px;
    }

    .btn-back-cards {
      background: #FFFDF9;
      border: 1px solid var(--rose-pink);
      color: var(--plum-ink);
      font-family: var(--font-sans);
      font-size: 0.95rem;
      font-weight: 700;
      padding: 9px 20px;
      border-radius: 9999px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 12px rgba(61, 38, 51, 0.08);
      transition: background 0.2s ease, transform 0.2s ease, color 0.2s ease;
    }

    .btn-back-cards:hover {
      background: var(--rose-pink);
      color: #FFF;
      transform: translateX(-4px);
    }

    .page-step-tag {
      font-family: var(--font-hand);
      font-size: 1.35rem;
      color: var(--plum-ink);
      font-weight: 700;
    }

    .page-prev-next-box {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .btn-step-circle {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: #FFFDF9;
      border: 1px solid rgba(201, 166, 107, 0.4);
      color: var(--plum-ink);
      font-size: 1.25rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
      transition: transform 0.2s ease, background 0.2s ease;
    }

    .btn-step-circle:hover {
      background: #FFF;
      transform: scale(1.1);
    }

    .page-story-wrapper {
      max-width: 920px;
      margin: 0 auto;
      background: #FFFDF9;
      border: 1px solid rgba(201, 166, 107, 0.35);
      border-radius: 16px;
      padding: clamp(28px, 4.5vw, 48px);
      box-shadow: 0 20px 40px -10px rgba(61, 38, 51, 0.15);
      position: relative;
    }

    .story-hero-two-col {
      display: grid;
      grid-template-columns: minmax(260px, 360px) 1fr;
      gap: clamp(20px, 3.5vw, 40px);
      align-items: center;
    }

    @media (max-width: 768px) {
      .story-hero-two-col {
        grid-template-columns: 1fr;
      }
    }

    .story-photo-polaroid-frame {
      background: #FFFFFF;
      padding: 14px 14px 28px 14px;
      border-radius: 4px;
      box-shadow: var(--shadow-polaroid);
      text-align: center;
      max-width: 380px;
      margin: 0 auto;
    }

    .story-photo-polaroid-frame img {
      width: 100%;
      aspect-ratio: 3 / 4;
      object-fit: cover;
      object-position: center 2%;
      display: block;
      border-radius: 2px;
    }

    .story-img-baby {
      aspect-ratio: 3 / 4;
      object-fit: cover;
      object-position: center 2%;
    }

    .story-img-family {
      aspect-ratio: 4 / 3;
      object-fit: cover;
      object-position: center 65%;
    }

    .story-photo-caption {
      margin-top: 12px;
      font-family: var(--font-hand);
      font-size: 1.4rem;
      color: var(--plum-ink);
      font-weight: 700;
    }

    .story-tag-pill {
      display: inline-block;
      background: rgba(232, 160, 168, 0.25);
      color: #8C4054;
      font-family: var(--font-retro);
      font-size: 0.75rem;
      letter-spacing: 2px;
      padding: 4px 12px;
      border-radius: 9999px;
      text-transform: uppercase;
      margin-bottom: 12px;
    }

    .story-title {
      font-family: var(--font-headline);
      font-size: clamp(2.2rem, 3.8vw, 3.2rem);
      font-style: italic;
      color: var(--plum-ink);
      line-height: 1.15;
      margin-bottom: 16px;
    }

    .story-body-text {
      font-family: var(--font-hand);
      font-size: clamp(1.25rem, 2.1vh, 1.5rem);
      line-height: 1.6;
      color: var(--plum-soft);
      white-space: pre-line;
    }

    .story-signature {
      font-family: var(--font-script);
      font-size: 1.6rem;
      color: var(--rose-pink);
      text-align: right;
      margin-top: 22px;
    }

    /* Cake Stage in Independent Page */
    .cake-full-stage {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    .interactive-candle-row {
      display: flex;
      justify-content: center;
      gap: 14px;
      margin-bottom: 12px;
    }

    .interactive-candle-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      cursor: pointer;
    }

    .interactive-candle-item .flame {
      width: 14px;
      height: 22px;
      background: radial-gradient(ellipse at 50% 85%, #FFF 0%, #FFE98A 30%, #FF8A3D 70%, #E63946 100%);
      border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
      box-shadow: 0 0 14px #FFB703, 0 0 24px #FB8500;
      animation: flameWiggle 1.4s ease-in-out infinite alternate;
      transition: opacity 0.3s ease, transform 0.3s ease;
    }

    .interactive-candle-item.blown .flame {
      opacity: 0;
      transform: scale(0.2) translateY(-10px);
    }

    .interactive-candle-item .wick {
      width: 2px;
      height: 8px;
      background: #3B202C;
    }

    .interactive-candle-item .stick {
      width: 12px;
      height: 48px;
      border-radius: 4px 4px 1px 1px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    .btn-blow-all-big {
      background: var(--heart-red);
      color: #FFF;
      border: none;
      font-family: var(--font-sans);
      font-size: 1.05rem;
      font-weight: 700;
      padding: 12px 28px;
      border-radius: 9999px;
      margin-top: 24px;
      cursor: pointer;
      box-shadow: 0 6px 20px rgba(230, 57, 70, 0.4);
      transition: transform 0.2s ease;
    }

    .btn-blow-all-big:hover {
      transform: scale(1.05);
    }

    /* Cursor Trail */
    .cursor-trail {
      position: fixed;
      pointer-events: none;
      z-index: 9999;
      font-size: 16px;
      color: var(--rose-pink);
      transform: translate(-50%, -50%);
      transition: transform 0.6s ease-out, opacity 0.6s ease-out;
    }
  </style>
</head>
<body>

  <!-- Paper Texture Overlay -->
  <div class="film-grain">
    <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
      <filter id="noiseFilter">
        <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/>
      </filter>
      <rect width="100%" height="100%" filter="url(#noiseFilter)"/>
    </svg>
  </div>

  <!-- Confetti Canvas -->
  <canvas id="confettiCanvas"></canvas>

  <!-- ═══════════════════════════════════════════════════════════
       1. OPENING COVER ENVELOPE PAGE
       ═══════════════════════════════════════════════════════════ -->
  <div id="coverScreen" title="Click anywhere to open your birthday scrapbook!">
    <div class="cover-card-box">
      <div class="cover-tape-top"></div>
      <p class="cover-eyebrow">A Special Birthday Keepsake</p>
      <h1 class="cover-title">Happy Birthday, Mom!</h1>
      <p class="cover-subtitle">A handcrafted scrapbook of our deepest love, laughs & sweetest memories ♡</p>
      
      <div class="cover-seal-btn" id="btnOpenCover" title="Click to Break the Seal!">
        <span>♥</span>
      </div>

      <p class="cover-prompt">✨ Click to Open Your Scrapbook ✨</p>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════
       2. CONFINED SQUARE CARDS BOARD (ALL CARDS ARE UNIQUE SQUARES!)
       ═══════════════════════════════════════════════════════════ -->
  <main id="cardsBoard">

    <!-- Top floating controls with prominent PLAY button -->
    <header class="top-action-bar">
      <button id="btnTopCover" class="btn-top-pill" title="Return to cover envelope">
        <span>✉</span> Envelope
      </button>
      <button id="btnTopMusic" class="btn-top-pill" title="Play or pause birthday melody">
        <span class="vinyl-dot"></span>
        <span id="musicBtnLabel">▶ Play Birthday Melody</span>
      </button>
    </header>

    <!-- Background collaged newspaper clippings -->
    <div class="bg-newspaper-scrap scrap-tl">
      DAILY CHRONICLE • SPECIAL EDITION<br>
      "World's Greatest Mom Celebrated Today"<br>
      A lifetime of kindness, warmth, and grace...
    </div>
    <div class="bg-newspaper-scrap scrap-br">
      VINTAGE MEMORIES • ARCHIVE<br>
      Laughter, warm tea, infinite hugs, and milestones.
      Forever cherished.
    </div>

    <!-- ═══ THE CONFINED 4x2 SQUARE CARDS GRID (STRICTLY CONFINED • ZERO SCROLL) ═══ -->
    <div class="square-board-wrapper">
      <div class="square-cards-grid">

        <!-- ── SQUARE 1: RETRO BABY POLAROID ── -->
        <article class="square-card sq-card-polaroid-baby" data-card="card1" title="Click to open Chapter 1">
          <div class="sq-polaroid-tape"></div>
          <div class="sq-photo-frame">
            <img id="imgBabyPhoto" src="" alt="Mom holding baby girl in white ruffled dress" />
          </div>
          <p class="sq-polaroid-caption">Where my story began ♡</p>
        </article>

        <!-- ── SQUARE 2: VINTAGE TORN QUOTE ── -->
        <article class="square-card sq-card-quote" data-card="card3" title="Click to read full love letter">
          <div class="sq-torn-corner">NEWS<br>DAILY</div>
          <p class="sq-quote-text">
            “I love you for all that you are, all that you have been, and all that you will be.”
          </p>
          <p class="sq-quote-author">— Unknown</p>
        </article>

        <!-- ── SQUARE 3: SPOTIFY BRICK RED ── -->
        <article class="square-card sq-card-spotify-red" data-card="card6" title="Click to open Walking in the Wind song page">
          <div class="sq-spotify-header">
            <div class="sq-album-thumb">
              <svg viewBox="0 0 36 36" width="100%" height="100%">
                <rect width="36" height="36" fill="#421412"/>
                <circle cx="18" cy="18" r="12" fill="#1C0A09"/>
                <circle cx="18" cy="18" r="4" fill="#E8A0A8"/>
              </svg>
            </div>
            <div>
              <div class="sq-track-title">Walking in the Wind</div>
              <div class="sq-track-artist">One Direction • For Mom</div>
            </div>
          </div>

          <p class="sq-spotify-lyrics">
            “And I'll be by your side<br>Any time you're needing me”
          </p>

          <div class="sq-spotify-footer">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="#FFF" opacity="0.9">
              <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.503 17.308c-.216.353-.674.468-1.027.251-2.812-1.718-6.352-2.107-10.521-1.155-.403.092-.803-.16-.895-.562-.092-.403.16-.803.562-.895 4.567-1.042 8.477-.597 11.629 1.334.354.217.469.674.252 1.027zm1.468-3.262c-.272.443-.852.585-1.295.313-3.218-1.977-8.125-2.55-11.93-1.394-.499.151-1.026-.135-1.177-.633-.151-.498.135-1.026.633-1.177 4.352-1.32 9.76-.677 13.456 1.596.443.272.585.852.313 1.295zm.126-3.41c-3.858-2.29-10.223-2.502-13.904-1.385-.591.179-1.218-.16-1.397-.751-.179-.591.16-1.218.751-1.397 4.234-1.285 11.266-1.036 15.698 1.595.53.315.703 1.002.389 1.533-.314.53-1.002.703-1.537.405z"/>
            </svg>
            <span style="font-family: var(--font-hand); font-size: 0.95rem; color: #FFF;">Play Song →</span>
          </div>
        </article>

        <!-- ── SQUARE 4: UNPAID THERAPIST KRAFT ── -->
        <article class="square-card sq-card-therapist" data-card="card4" title="Click to read Unpaid Therapist tribute">
          <p class="sq-therapist-title">Thanks for being my unpaid therapist!</p>
          <svg class="sq-therapist-heart" viewBox="0 0 32 32">
            <path d="M16 28 C8 20 2 14 2 8 A6 6 0 0 1 14 5 L16 7 L18 5 A6 6 0 0 1 30 8 C30 14 24 20 16 28 Z" fill="#E63946"/>
          </svg>
          <span class="sq-therapist-sub">Available 24/7 with tea & love ♡</span>
        </article>

        <!-- ── SQUARE 5: BEST-TEA SQUARE ── -->
        <article class="square-card sq-card-best-tea" data-card="card2" title="Click to open Best-Tea Story">
          <p class="sq-best-tea-title">YOU'LL ALWAYS<br>♡ BE MY ♡<br>BEST-TEA</p>
          <svg viewBox="0 0 160 80" width="110" height="54" style="margin: auto 0;">
            <rect x="25" y="22" width="45" height="40" rx="10" fill="#F8B4B8" stroke="#3D2633" stroke-width="2.5"/>
            <path d="M25 33 Q10 38 25 52" fill="none" stroke="#3D2633" stroke-width="2.5"/>
            <circle cx="39" cy="39" r="2.5" fill="#3D2633"/>
            <circle cx="56" cy="39" r="2.5" fill="#3D2633"/>
            <path d="M44 45 Q47 49 51 45" fill="none" stroke="#3D2633" stroke-width="2" stroke-linecap="round"/>
            <rect x="85" y="22" width="45" height="40" rx="10" fill="#C5B3E6" stroke="#3D2633" stroke-width="2.5"/>
            <path d="M130 33 Q145 38 130 52" fill="none" stroke="#3D2633" stroke-width="2.5"/>
            <circle cx="99" cy="39" r="2.5" fill="#3D2633"/>
            <circle cx="116" cy="39" r="2.5" fill="#3D2633"/>
            <path d="M104 45 Q107 49 111 45" fill="none" stroke="#3D2633" stroke-width="2" stroke-linecap="round"/>
            <path d="M78 14 C74 10 70 13 72 17 L78 22 L84 17 C86 13 82 10 78 14 Z" fill="#E63946"/>
          </svg>
          <span style="font-family:var(--font-hand); font-size:0.92rem; color:#9E748B;">Our Sweet Memories ♡</span>
        </article>

        <!-- ── SQUARE 6: TEDDY BEAR BIRTHDAY CAKE SQUARE ── -->
        <article class="square-card sq-card-cake" data-card="card5" title="Click to open birthday cake page!">
          <svg viewBox="0 0 150 120" width="110" height="88">
            <ellipse cx="75" cy="114" rx="60" ry="6" fill="#E6DFD5"/>
            <rect x="28" y="80" width="94" height="30" rx="5" fill="#FDF7EE" stroke="#3D2633" stroke-width="2.5"/>
            <path d="M28 80 Q38 90 48 80 Q58 90 68 80 Q78 90 88 80 Q98 90 108 80 Q118 90 122 80" fill="#FCE5E7" stroke="#3D2633" stroke-width="2"/>
            <rect x="44" y="52" width="62" height="28" rx="5" fill="#FDF7EE" stroke="#3D2633" stroke-width="2.5"/>
            <path d="M44 52 Q52 60 60 52 Q68 60 76 52 Q84 60 92 52 Q100 60 106 52" fill="#FCE5E7" stroke="#3D2633" stroke-width="2"/>
            <!-- Teddy Bear Topper -->
            <circle cx="64" cy="30" r="7.5" fill="#936248" stroke="#3D2633" stroke-width="1.8"/>
            <circle cx="86" cy="30" r="7.5" fill="#936248" stroke="#3D2633" stroke-width="1.8"/>
            <ellipse cx="75" cy="38" rx="16" ry="14" fill="#936248" stroke="#3D2633" stroke-width="1.8"/>
            <ellipse cx="75" cy="41" rx="7" ry="5" fill="#FCE5CE"/>
            <ellipse cx="75" cy="39" rx="2.5" ry="1.5" fill="#3D2633"/>
            <!-- Party Hat & Candle -->
            <polygon points="75,18 69,28 81,28" fill="#6DA5C0" stroke="#3D2633" stroke-width="1.8"/>
            <rect x="73.5" y="8" width="3" height="10" fill="#FFE98A" stroke="#3D2633" stroke-width="1.2"/>
            <!-- Candle Flame -->
            <g class="cake-flame-svg" id="boardCakeFlame">
              <ellipse cx="75" cy="5" rx="5" ry="7" fill="#FF8A3D"/>
              <ellipse cx="75" cy="6" rx="2.5" ry="4" fill="#FFF"/>
            </g>
          </svg>
          <span class="sq-cake-prompt">Tap to blow candle! ✨</span>
        </article>

        <!-- ── SQUARE 7: SPOTIFY WHITE SQUARE ── -->
        <article class="square-card sq-card-spotify-white" data-card="card7" title="Click to open Best Friend tribute">
          <div class="sq-spotify-header">
            <div class="sq-album-thumb" style="background:#222;">
              <svg viewBox="0 0 36 36" width="100%" height="100%">
                <rect width="36" height="36" fill="#222"/>
                <polygon points="14,10 26,18 14,26" fill="#FFF"/>
              </svg>
            </div>
            <div>
              <div class="sq-track-title" style="color:#111;">You Get Me So High</div>
              <div class="sq-track-artist" style="color:#666;">The Neighbourhood</div>
            </div>
          </div>

          <div>
            <p class="sq-white-quote">
              You're my best friend,<br>I'll love you forever ♥
            </p>
            <div class="sq-pink-line"></div>
          </div>

          <div class="sq-spotify-footer" style="border-top-color:#EEE;">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="#1DB954">
              <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.503 17.308c-.216.353-.674.468-1.027.251-2.812-1.718-6.352-2.107-10.521-1.155-.403.092-.803-.16-.895-.562-.092-.403.16-.803.562-.895 4.567-1.042 8.477-.597 11.629 1.334.354.217.469.674.252 1.027zm1.468-3.262c-.272.443-.852.585-1.295.313-3.218-1.977-8.125-2.55-11.93-1.394-.499.151-1.026-.135-1.177-.633-.151-.498.135-1.026.633-1.177 4.352-1.32 9.76-.677 13.456 1.596.443.272.585.852.313 1.295zm.126-3.41c-3.858-2.29-10.223-2.502-13.904-1.385-.591.179-1.218-.16-1.397-.751-.179-.591.16-1.218.751-1.397 4.234-1.285 11.266-1.036 15.698 1.595.53.315.703 1.002.389 1.533-.314.53-1.002.703-1.537.405z"/>
            </svg>
            <span style="font-family:var(--font-hand); font-size:0.92rem; color:#888;">Tribute Page →</span>
          </div>
        </article>

        <!-- ── SQUARE 8: FAMILY MILESTONE POLAROID ── -->
        <article class="square-card sq-card-polaroid-family" data-card="card8" title="Click to view Family Milestone">
          <div class="sq-family-tape"></div>
          <div class="sq-photo-frame">
            <img id="imgFamilyPhoto" src="" alt="Family at stone temple steps" />
          </div>
          <p class="sq-polaroid-caption">Together through milestones ♡</p>
        </article>

      </div>
    </div>

    <!-- ═══ FLOATING STICKERS & DOODLES (AROUND SQUARES) ═══ -->
    <div class="sticker-floating sticker-lungs" title="You Be-Lung To Me ♡">
      <svg viewBox="0 0 120 100" width="100%">
        <path d="M60 10 L60 45 M60 45 Q40 50 25 70 Q15 85 28 92 Q42 96 52 75 L55 52 M60 45 Q80 50 95 70 Q105 85 92 92 Q78 96 68 75 L65 52" fill="none" stroke="#2B7A78" stroke-width="4" stroke-linecap="round"/>
        <path d="M25 50 Q10 65 20 85 Q35 96 50 78 Q55 60 40 48 Z" fill="#FF5D8F" stroke="#3D2633" stroke-width="2.5"/>
        <path d="M95 50 Q110 65 100 85 Q85 96 70 78 Q65 60 80 48 Z" fill="#FF5D8F" stroke="#3D2633" stroke-width="2.5"/>
        <line x1="45" y1="65" x2="75" y2="65" stroke="#3D2633" stroke-width="2"/>
        <rect x="8" y="82" width="104" height="15" rx="3" fill="#FFF" stroke="#3D2633" stroke-width="1.5"/>
        <text x="60" y="93" font-family="'Special Elite', monospace" font-size="8.5" font-weight="bold" fill="#111" text-anchor="middle">YOU BE-LUNG TO ME</text>
      </svg>
    </div>

    <div class="sticker-floating sticker-huggers" title="Big Hugs for Mom!">
      <svg viewBox="0 0 90 90" width="100%">
        <circle cx="32" cy="45" r="22" fill="#FFFDF9" stroke="#3D2633" stroke-width="2.5"/>
        <circle cx="58" cy="45" r="22" fill="#FFFDF9" stroke="#3D2633" stroke-width="2.5"/>
        <circle cx="26" cy="42" r="2.5" fill="#3D2633"/>
        <circle cx="38" cy="42" r="2.5" fill="#3D2633"/>
        <circle cx="52" cy="42" r="2.5" fill="#3D2633"/>
        <circle cx="64" cy="42" r="2.5" fill="#3D2633"/>
        <path d="M30 48 Q32 52 34 48" fill="none" stroke="#3D2633" stroke-width="2"/>
        <path d="M56 48 Q58 52 60 48" fill="none" stroke="#3D2633" stroke-width="2"/>
        <path d="M45 22 C42 16 34 20 38 27 L45 33 L52 27 C56 20 48 16 45 22 Z" fill="#FF4D6D"/>
      </svg>
    </div>

    <div class="sticker-floating sticker-hbd-banner" title="Happy Birthday to You!">
      <svg viewBox="0 0 140 70" width="100%">
        <rect x="4" y="4" width="132" height="62" rx="4" fill="#FFFFFF" stroke="#3D2633" stroke-width="2" filter="drop-shadow(2px 3px 4px rgba(0,0,0,0.15))"/>
        <text x="70" y="28" font-family="'Caveat', cursive" font-size="20" font-weight="bold" fill="#1A1A1A" text-anchor="middle">★ HAPPY ★</text>
        <text x="70" y="52" font-family="'Caveat', cursive" font-size="24" font-weight="bold" fill="#1A1A1A" text-anchor="middle">Birthday to you</text>
      </svg>
    </div>

    <div class="sticker-floating sticker-rose" title="A Sweet Rose for Mom">
      <svg viewBox="0 0 120 60" width="100%">
        <rect x="36" y="32" width="80" height="20" fill="#D8C7B5" opacity="0.9" transform="rotate(-3 76 42)"/>
        <text x="76" y="46" font-family="'Special Elite', monospace" font-size="7.5" font-weight="bold" fill="#332211" text-anchor="middle">SWEETEST THING</text>
        <circle cx="22" cy="18" r="12" fill="#E63946" stroke="#3D2633" stroke-width="2"/>
        <line x1="22" y1="30" x2="22" y2="55" stroke="#406343" stroke-width="3" stroke-linecap="round"/>
      </svg>
    </div>

    <div class="sticker-floating sticker-puzzle" title="Connecting Puzzle Pieces!">
      <svg viewBox="0 0 85 45" width="100%">
        <rect x="4" y="6" width="36" height="32" rx="3" fill="#FFFDF9" stroke="#3D2633" stroke-width="2"/>
        <circle cx="40" cy="22" r="6" fill="#FFFDF9" stroke="#3D2633" stroke-width="2"/>
        <rect x="44" y="6" width="36" height="32" rx="3" fill="#FFFDF9" stroke="#3D2633" stroke-width="2"/>
        <circle cx="20" cy="20" r="1.8" fill="#3D2633"/>
        <circle cx="28" cy="20" r="1.8" fill="#3D2633"/>
        <circle cx="58" cy="20" r="1.8" fill="#3D2633"/>
        <circle cx="66" cy="20" r="1.8" fill="#3D2633"/>
      </svg>
    </div>

  </main>

  <!-- ═══════════════════════════════════════════════════════════
       3. INDEPENDENT DEDICATED STORY PAGES VIEW
       ═══════════════════════════════════════════════════════════ -->
  <section id="detailPageView">
    <nav class="page-nav-bar">
      <button class="btn-back-cards" id="btnBackToCards" title="Return to Square Cards Board">
        ← Back to Board
      </button>

      <span class="page-step-tag" id="pageStepTag">Where My Story Began</span>

      <div class="page-prev-next-box">
        <button class="btn-step-circle" id="btnPrevCard" title="Previous Story (Left Arrow)">‹</button>
        <button class="btn-step-circle" id="btnNextCard" title="Next Story (Right Arrow)">›</button>
      </div>
    </nav>

    <div class="page-story-wrapper" id="storyContentContainer">
      <!-- Injected dynamically via JS based on clicked card -->
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════════════
       JAVASCRIPT LOGIC
       ═══════════════════════════════════════════════════════════ -->
  <script>
    ''' + images_code + '''

    // Inject base64 images into board polaroids
    document.getElementById('imgBabyPhoto').src = PHOTO_MOM_BABY;
    document.getElementById('imgFamilyPhoto').src = PHOTO_MOM_FAMILY;

    /* ═══════════════════════════════════════════════════════════
       WEB AUDIO SYNTHESIZER (MUSIC & CHIMES)
       ═══════════════════════════════════════════════════════════ */
    class BirthdayAudioSynth {
      constructor() {
        this.ctx = null;
        this.isPlaying = false;
        this.timer = null;
      }

      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          this.ctx = new AudioContext();
          this.masterGain = this.ctx.createGain();
          this.masterGain.gain.setValueAtTime(0.3, this.ctx.currentTime);
          this.masterGain.connect(this.ctx.destination);
        }
        if (this.ctx.state === 'suspended') {
          this.ctx.resume();
        }
      }

      playTone(freq, time, dur, vol = 0.2) {
        if (!this.ctx) return;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, time);

        gain.gain.setValueAtTime(0.001, time);
        gain.gain.linearRampToValueAtTime(vol, time + 0.05);
        gain.gain.exponentialRampToValueAtTime(0.0001, time + dur);

        osc.connect(gain);
        gain.connect(this.masterGain);
        osc.start(time);
        osc.stop(time + dur);
      }

      playChime() {
        try {
          this.init();
          if (!this.ctx) return;
          const notes = [523.25, 659.25, 783.99, 1046.5];
          const now = this.ctx.currentTime;
          notes.forEach((f, i) => this.playTone(f, now + i * 0.07, 1.0, 0.25));
        } catch(e) {}
      }

      startMelody() {
        try {
          this.init();
          if (this.isPlaying) return;
          this.isPlaying = true;

          const melody = [
            { f: 261.63, d: 0.35, p: 0.4 }, { f: 261.63, d: 0.3, p: 0.35 },
            { f: 293.66, d: 0.6, p: 0.7 }, { f: 261.63, d: 0.6, p: 0.7 },
            { f: 349.23, d: 0.6, p: 0.7 }, { f: 329.63, d: 1.1, p: 1.3 },
            { f: 261.63, d: 0.35, p: 0.4 }, { f: 261.63, d: 0.3, p: 0.35 },
            { f: 293.66, d: 0.6, p: 0.7 }, { f: 261.63, d: 0.6, p: 0.7 },
            { f: 392.00, d: 0.6, p: 0.7 }, { f: 349.23, d: 1.1, p: 1.3 },
            { f: 261.63, d: 0.35, p: 0.4 }, { f: 261.63, d: 0.3, p: 0.35 },
            { f: 523.25, d: 0.7, p: 0.8 }, { f: 440.00, d: 0.7, p: 0.8 },
            { f: 349.23, d: 0.6, p: 0.7 }, { f: 329.63, d: 0.6, p: 0.7 },
            { f: 293.66, d: 1.1, p: 1.3 }, { f: 466.16, d: 0.35, p: 0.4 },
            { f: 466.16, d: 0.3, p: 0.35 }, { f: 440.00, d: 0.7, p: 0.8 },
            { f: 349.23, d: 0.6, p: 0.7 }, { f: 392.00, d: 0.8, p: 0.9 },
            { f: 349.23, d: 1.5, p: 2.2 }
          ];

          let idx = 0;
          const step = () => {
            if (!this.isPlaying) return;
            const note = melody[idx];
            const now = this.ctx ? this.ctx.currentTime : 0;
            this.playTone(note.f, now, note.d * 1.4, 0.22);
            this.playTone(note.f * 1.5, now + 0.04, note.d * 1.1, 0.06);
            idx = (idx + 1) % melody.length;
            this.timer = setTimeout(step, note.p * 1000);
          };
          step();
          updateMusicUI(true);
        } catch(e) {}
      }

      stopMelody() {
        this.isPlaying = false;
        if (this.timer) {
          clearTimeout(this.timer);
          this.timer = null;
        }
        updateMusicUI(false);
      }

      toggle() {
        if (this.isPlaying) this.stopMelody();
        else this.startMelody();
      }
    }

    const sound = new BirthdayAudioSynth();

    function updateMusicUI(playing) {
      const btn = document.getElementById('btnTopMusic');
      const label = document.getElementById('musicBtnLabel');
      if (playing) {
        btn.classList.add('playing');
        label.textContent = '⏸ Pause Melody';
      } else {
        btn.classList.remove('playing');
        label.textContent = '▶ Play Birthday Melody';
      }
    }

    document.getElementById('btnTopMusic').addEventListener('click', () => {
      sound.toggle();
    });

    /* ═══════════════════════════════════════════════════════════
       CONFETTI SYSTEM
       ═══════════════════════════════════════════════════════════ */
    const cCanvas = document.getElementById('confettiCanvas');
    const cCtx = cCanvas.getContext('2d');
    let confetti = [];

    function resizeCanvas() {
      cCanvas.width = window.innerWidth;
      cCanvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    const confettiColors = ['#F9D8D6', '#E8A0A8', '#FFF8F0', '#FBE9B7', '#D9CCF0', '#C7D3B8', '#D4AF37'];

    class Confetto {
      constructor(x, y) {
        this.x = x;
        this.y = y;
        const angle = Math.random() * Math.PI * 2;
        const speed = Math.random() * 9 + 4;
        this.vx = Math.cos(angle) * speed;
        this.vy = Math.sin(angle) * speed - 2;
        this.gravity = 0.22;
        this.drag = 0.96;
        this.size = Math.random() * 8 + 5;
        this.color = confettiColors[Math.floor(Math.random() * confettiColors.length)];
        this.rot = Math.random() * 360;
        this.rotSpeed = (Math.random() - 0.5) * 8;
        this.opacity = 1;
        this.decay = Math.random() * 0.008 + 0.006;
      }
      update() {
        this.vx *= this.drag;
        this.vy *= this.drag;
        this.vy += this.gravity;
        this.x += this.vx;
        this.y += this.vy;
        this.rot += this.rotSpeed;
        this.opacity -= this.decay;
      }
      draw(ctx) {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate((this.rot * Math.PI) / 180);
        ctx.globalAlpha = Math.max(0, this.opacity);
        ctx.fillStyle = this.color;
        ctx.fillRect(-this.size / 2, -this.size / 4, this.size, this.size / 2);
        ctx.restore();
      }
    }

    function burstConfetti(x, y, count = 75) {
      for (let i = 0; i < count; i++) confetti.push(new Confetto(x, y));
    }

    function animateConfetti() {
      cCtx.clearRect(0, 0, cCanvas.width, cCanvas.height);
      for (let i = confetti.length - 1; i >= 0; i--) {
        const p = confetti[i];
        p.update();
        p.draw(cCtx);
        if (p.opacity <= 0 || p.y > window.innerHeight + 50) confetti.splice(i, 1);
      }
      requestAnimationFrame(animateConfetti);
    }
    animateConfetti();

    /* ═══════════════════════════════════════════════════════════
       VIEW TRANSITIONS: COVER <-> CONFINED BOARD <-> STORY PAGE
       ═══════════════════════════════════════════════════════════ */
    const coverScreen = document.getElementById('coverScreen');
    const btnOpenCover = document.getElementById('btnOpenCover');
    const btnTopCover = document.getElementById('btnTopCover');
    const cardsBoard = document.getElementById('cardsBoard');
    const detailPageView = document.getElementById('detailPageView');
    const storyContentContainer = document.getElementById('storyContentContainer');
    const btnBackToCards = document.getElementById('btnBackToCards');
    const btnPrevCard = document.getElementById('btnPrevCard');
    const btnNextCard = document.getElementById('btnNextCard');
    const pageStepTag = document.getElementById('pageStepTag');

    const cardKeys = ['card1', 'card3', 'card6', 'card4', 'card2', 'card5', 'card7', 'card8'];
    const cardTitles = [
      "Where My Story Began",
      "The Greatest Gift of All",
      "Walking in the Wind",
      "My Unpaid Therapist & Anchor",
      "You'll Always Be My Best-Tea",
      "The Birthday Wish & Cake",
      "My Best Friend, Forever",
      "Together Through Every Milestone"
    ];
    let currentCardIndex = 0;

    function openScrapbook() {
      sound.playChime();
      coverScreen.classList.add('opened');
      burstConfetti(window.innerWidth / 2, window.innerHeight / 2, 85);
      setTimeout(() => {
        if (!sound.isPlaying) sound.startMelody();
      }, 500);
    }

    function returnToCover() {
      detailPageView.style.display = 'none';
      cardsBoard.style.display = 'flex';
      coverScreen.classList.remove('opened');
      sound.playChime();
    }

    coverScreen.addEventListener('click', openScrapbook);
    btnOpenCover.addEventListener('click', (e) => {
      e.stopPropagation();
      openScrapbook();
    });
    btnTopCover.addEventListener('click', returnToCover);

    // Clicking ANY square card on the board opens its independent page!
    document.querySelectorAll('.square-card').forEach(card => {
      card.addEventListener('click', () => {
        const key = card.dataset.card;
        currentCardIndex = cardKeys.indexOf(key);
        showIndependentPage(currentCardIndex);
      });
    });

    function showIndependentPage(idx) {
      sound.playChime();
      currentCardIndex = idx;
      pageStepTag.textContent = `${idx + 1} of 8 • ${cardTitles[idx]}`;

      renderIndependentPage(cardKeys[idx]);

      cardsBoard.style.display = 'none';
      detailPageView.style.display = 'block';
      window.scrollTo({ top: 0, behavior: 'smooth' });
      burstConfetti(window.innerWidth / 2, 180, 45);
    }

    function backToCardsBoard() {
      sound.playChime();
      detailPageView.style.display = 'none';
      cardsBoard.style.display = 'flex';
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    btnBackToCards.addEventListener('click', backToCardsBoard);

    btnPrevCard.addEventListener('click', () => {
      currentCardIndex = (currentCardIndex - 1 + cardKeys.length) % cardKeys.length;
      showIndependentPage(currentCardIndex);
    });

    btnNextCard.addEventListener('click', () => {
      currentCardIndex = (currentCardIndex + 1) % cardKeys.length;
      showIndependentPage(currentCardIndex);
    });

    document.addEventListener('keydown', (e) => {
      if (detailPageView.style.display === 'block') {
        if (e.key === 'Escape') backToCardsBoard();
        if (e.key === 'ArrowLeft') btnPrevCard.click();
        if (e.key === 'ArrowRight') btnNextCard.click();
      }
    });

    // Cake flame click on board
    const boardCakeFlame = document.getElementById('boardCakeFlame');
    if (boardCakeFlame) {
      boardCakeFlame.addEventListener('click', (e) => {
        e.stopPropagation();
        sound.playChime();
        boardCakeFlame.classList.toggle('blown');
        burstConfetti(e.clientX, e.clientY, 50);
      });
    }

    /* ═══════════════════════════════════════════════════════════
       RENDER INDEPENDENT DEDICATED STORY PAGES
       ═══════════════════════════════════════════════════════════ */
    function renderIndependentPage(key) {
      if (key === 'card1') {
        // CARD 1: MOM & BABY
        storyContentContainer.innerHTML = `
          <div class="story-hero-two-col">
            <div class="story-photo-polaroid-frame" style="transform: rotate(-1.5deg);">
              <img class="story-img-baby" src="${PHOTO_MOM_BABY}" alt="Mom holding baby girl in white dress" />
              <p class="story-photo-caption">Where my story began ♡</p>
            </div>
            <div>
              <span class="story-tag-pill">Chapter One • Endless Love</span>
              <h2 class="story-title">Held in Your Arms from the Start</h2>
              <div class="story-body-text">
                Dearest Mom,

                Long before I knew what the world was, I knew the gentle warmth of your embrace and the softness of your voice singing me to sleep.

                In this photograph, you held me in that delicate white dress—and ever since that day, you have protected my dreams, cheered my tiniest victories, and given me a world of unconditional safety.

                Everything beautiful and compassionate in my life was planted by your loving hands.
              </div>
              <div class="story-signature">— With infinite love & gratitude ♡</div>
            </div>
          </div>
        `;
      }
      else if (key === 'card2') {
        // CARD 2: BEST-TEA
        storyContentContainer.innerHTML = `
          <div style="max-width: 720px; margin: 0 auto; text-align: center;">
            <span class="story-tag-pill">A Warm Cup of Love</span>
            <h2 class="story-title">You'll Always Be My Best-Tea</h2>
            <div class="story-body-text">
              Mom, nothing in this world comforts the soul quite like sitting across the kitchen table with you, sipping hot tea, and talking about everything and nothing at all.

              You know every secret glance, you celebrate my good news before anyone else, and your laughter is the coziest sound in our home.

              Here is to a million more warm cups of tea and heartwarming chats with my forever best friend!
            </div>
            <div class="story-signature" style="text-align: center;">— Steeped in love forever ♡</div>
          </div>
        `;
      }
      else if (key === 'card3') {
        // CARD 3: TORN QUOTE
        storyContentContainer.innerHTML = `
          <div style="max-width: 760px; margin: 0 auto; text-align: center;">
            <span class="story-tag-pill">From the Depth of My Heart</span>
            <h2 class="story-title">“I love you for all that you are...”</h2>
            <div class="story-body-text">
              “...all that you have been, and all that you will ever be.”

              Mom, as the years turn, my appreciation for your quiet sacrifices only deepens. You gave so much of yourself so that we could flourish. 

              You taught me grace when life was stormy, and kindness when the world was harsh. 

              May today shower you with the same pure joy that you have poured into our lives every single sunrise.
            </div>
            <div class="story-signature" style="text-align: center;">— Your devoted child ♡</div>
          </div>
        `;
      }
      else if (key === 'card4') {
        // CARD 4: UNPAID THERAPIST
        storyContentContainer.innerHTML = `
          <div style="max-width: 740px; margin: 0 auto; text-align: center;">
            <span class="story-tag-pill">Official Recognition</span>
            <h2 class="story-title">Thanks for Being My Unpaid Therapist!</h2>
            <div class="story-body-text">
              Mom, your office hours are 24/7/365, your hugs cure any heartbreak, and your advice is always 100% right (even when I stubborn-headedly take a week to admit it!).

              Thank you for never judging my late-night rambles, for keeping every secret locked safe in your heart, and for always being the calm harbor in every storm.

              You truly are the greatest listener, comforter, and life advisor on this planet.
            </div>
            <div class="story-signature" style="text-align: center;">— Five stars across the board ★★★★★</div>
          </div>
        `;
      }
      else if (key === 'card5') {
        // CARD 5: CAKE & WISHES
        storyContentContainer.innerHTML = `
          <div class="cake-full-stage">
            <span class="story-tag-pill">Interactive Celebration</span>
            <h2 class="story-title">Make a Secret Birthday Wish!</h2>
            <p style="font-family: var(--font-hand); font-size: 1.45rem; color: var(--plum-soft); margin-bottom: 22px;">
              Tap each candle below to blow out its flame, then make your deepest wish!
            </p>

            <div class="interactive-candle-row" id="pageCandleRow">
              <div class="interactive-candle-item"><div class="flame"></div><div class="wick"></div><div class="stick" style="background:#F6D6D6;"></div></div>
              <div class="interactive-candle-item"><div class="flame"></div><div class="wick"></div><div class="stick" style="background:#FBE9B7;"></div></div>
              <div class="interactive-candle-item"><div class="flame"></div><div class="wick"></div><div class="stick" style="background:#D9CCF0; height:56px;"></div></div>
              <div class="interactive-candle-item"><div class="flame"></div><div class="wick"></div><div class="stick" style="background:#C7D3B8; height:56px;"></div></div>
              <div class="interactive-candle-item"><div class="flame"></div><div class="wick"></div><div class="stick" style="background:#FBE9B7;"></div></div>
              <div class="interactive-candle-item"><div class="flame"></div><div class="wick"></div><div class="stick" style="background:#F6D6D6;"></div></div>
            </div>

            <svg viewBox="0 0 280 180" width="230" height="145">
              <ellipse cx="140" cy="170" rx="125" ry="10" fill="rgba(61,38,51,0.12)" />
              <rect x="45" y="115" width="190" height="50" rx="8" fill="#FCE5E7" stroke="#3D2633" stroke-width="2.5"/>
              <rect x="75" y="70" width="130" height="46" rx="6" fill="#FFFDF9" stroke="#3D2633" stroke-width="2.5"/>
              <circle cx="120" cy="40" r="14" fill="#936248" stroke="#3D2633" stroke-width="2"/>
              <circle cx="160" cy="40" r="14" fill="#936248" stroke="#3D2633" stroke-width="2"/>
              <ellipse cx="140" cy="50" rx="24" ry="20" fill="#936248" stroke="#3D2633" stroke-width="2"/>
              <ellipse cx="140" cy="54" rx="10" ry="7" fill="#FCE5CE"/>
              <circle cx="140" cy="51" r="3" fill="#3D2633"/>
              <polygon points="140,16 130,34 150,34" fill="#6DA5C0" stroke="#3D2633" stroke-width="2"/>
              <circle cx="140" cy="16" r="4" fill="#FFB703"/>
            </svg>

            <button class="btn-blow-all-big" id="btnBlowAllCandles">
              🎂 Blow Out All Candles & Make a Wish!
            </button>

            <div id="cakeWishMessage" style="display:none; margin-top:20px; font-family:var(--font-hand); font-size:1.85rem; color:#E63946; font-weight:bold;">
              ✨ Happy Birthday Mom! May all your secret prayers come true! ✨
            </div>
          </div>
        `;

        document.querySelectorAll('#pageCandleRow .interactive-candle-item').forEach(c => {
          c.addEventListener('click', () => {
            sound.playChime();
            c.classList.toggle('blown');
            burstConfetti(window.innerWidth / 2, 280, 30);
          });
        });

        document.getElementById('btnBlowAllCandles').addEventListener('click', () => {
          sound.playChime();
          const items = document.querySelectorAll('#pageCandleRow .interactive-candle-item');
          items.forEach(c => c.classList.add('blown'));
          burstConfetti(window.innerWidth / 2, 250, 100);
          document.getElementById('cakeWishMessage').style.display = 'block';
        });
      }
      else if (key === 'card6') {
        // CARD 6: WALKING IN THE WIND (SPOTIFY RED)
        storyContentContainer.innerHTML = `
          <div style="max-width: 760px; margin: 0 auto; text-align: center;">
            <span class="story-tag-pill">One Direction • For Mom</span>
            <h2 class="story-title">Walking in the Wind</h2>
            <div class="story-body-text">
              “A week of charming friendship and a month of love<br>
              And I'll be by your side, any time you're needing me<br>
              You're in my heart, even when you're a thousand miles away.”

              Mom, no matter where life leads or how far we travel, your love is the compass that guides us home. 

              You walk beside us through every storm and every triumph. Today we celebrate the amazing woman who makes our world so warm.
            </div>
            <div style="margin-top: 24px;">
              <button class="btn-back-cards" id="btnPlaySongTribute" style="background: var(--spotify-brick); color: #FFF; font-size: 1.05rem;">
                ▶ Play Melody
              </button>
            </div>
            <div class="story-signature" style="text-align: center;">— Always by your side ♡</div>
          </div>
        `;
        document.getElementById('btnPlaySongTribute').addEventListener('click', () => {
          sound.toggle();
        });
      }
      else if (key === 'card7') {
        // CARD 7: BEST FRIEND (SPOTIFY WHITE)
        storyContentContainer.innerHTML = `
          <div style="max-width: 740px; margin: 0 auto; text-align: center;">
            <span class="story-tag-pill">The Neighbourhood • Dedication</span>
            <h2 class="story-title">You're My Best Friend, I'll Love You Forever</h2>
            <div class="story-body-text">
              Mom, mothers are many things—teachers, protectors, caregivers—but having you as my best friend has been the rarest blessing of all.

              You understand without words, you forgive without grudge, and your belief in me gave me wings when I doubted myself.

              I will cherish and love you through every season, every laughter, and every milestone.
            </div>
            <div class="story-signature" style="text-align: center;">— Forever your #1 fan ♡</div>
          </div>
        `;
      }
      else if (key === 'card8') {
        // CARD 8: FAMILY AT TEMPLE
        storyContentContainer.innerHTML = `
          <div class="story-hero-two-col">
            <div class="story-photo-polaroid-frame" style="transform: rotate(1deg);">
              <img class="story-img-family" src="${PHOTO_MOM_FAMILY}" alt="Mom with grown son and daughter at stone temple steps" />
              <p class="story-photo-caption">Together through every milestone ♡</p>
            </div>
            <div>
              <span class="story-tag-pill">Family Milestone • Eternal Bond</span>
              <h2 class="story-title">Together Through Every Step</h2>
              <div class="story-body-text">
                Dearest Mom,

                Sitting beside you on those carved temple steps, looking at how far our family has walked together, filled our hearts with awe.

                From the days of baby steps in your arms to sitting tall as grown adults beside you, you were the quiet powerhouse behind every triumph.

                You gave us roots to ground us and wings to soar. Today, we celebrate YOU—our queen, our heart, our greatest hero.
              </div>
              <div class="story-signature">— With all our love, always & forever ♡</div>
            </div>
          </div>
        `;
      }
    }

    /* ═══════════════════════════════════════════════════════════
       CURSOR HEART TRAIL
       ═══════════════════════════════════════════════════════════ */
    if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      let lastTime = 0;
      window.addEventListener('mousemove', (e) => {
        const now = Date.now();
        if (now - lastTime < 50) return;
        lastTime = now;

        const h = document.createElement('div');
        h.className = 'cursor-trail';
        h.textContent = '♡';
        h.style.left = `${e.clientX}px`;
        h.style.top = `${e.clientY}px`;
        document.body.appendChild(h);

        setTimeout(() => {
          h.style.transform = `translate(-50%, -120%) scale(1.4)`;
          h.style.opacity = '0';
        }, 20);

        setTimeout(() => h.remove(), 600);
      });
    }

    /* ═══════════════════════════════════════════════════════════
       URL & HASH ROUTING
       ═══════════════════════════════════════════════════════════ */
    window.addEventListener('DOMContentLoaded', () => {
      const urlParams = new URLSearchParams(window.location.search);
      const hash = window.location.hash;
      if (urlParams.get('view') === 'board' || hash === '#board') {
        openScrapbook();
      } else if (urlParams.get('card')) {
        openScrapbook();
        const cardKey = urlParams.get('card');
        const idx = cardKeys.indexOf(cardKey);
        if (idx !== -1) showIndependentPage(idx);
      }
    });
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Built optimized square cards app successfully!")
