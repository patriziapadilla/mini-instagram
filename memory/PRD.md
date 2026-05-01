# D'Royal Spa Home-3D — Scroll Direction Conversion

## Problem Statement
From GitHub repo `patriziapadilla/D-Royal-Spa-Home-3D` (originally `mini-instagram`), folder `home-3d`: convert the horizontal scroll to vertical scroll (top to bottom). Keep ALL buttons, content, videos and design exactly as they are. Add fully immersive 3D scroll-based motion with depth, parallax, and interactive elements responding to scroll.

## User Choices
- Access: Clone from GitHub (public repo)
- Reveal animation: Fade-in + upward translate (extended with 3D depth on user request)
- Scroll behavior: Snap to each section (y mandatory)
- Replace existing version (in-place edits to `home-3d/index.html`)

## Implementation (Jan 2026)
Single-file edit to `/app/home-3d/index.html`:

### CSS
- `.deck`: `overflow-x: hidden`, `overflow-y: auto`, `scroll-snap-type: y mandatory`, `flex-direction: column`, `perspective: 1400px`
- `.slide`: `flex: 0 0 100vh`, `width: 100%`, `transform-style: preserve-3d`, CSS vars `--p`/`--abs-p` for scroll progress
- `.slide-inner`: 3D entry transform (translateZ -140px, rotateX 10°, scale .96) → active state (0, 0, 1)
- Parallax layers: `.home-video`, `.media-stage video/img` translate & scale by `--p`; `.home-center`/`.treatment-wrap` counter-translate; `.home-rail` translate by `--p`
- Staggered child reveals on `.slide.active` (home-center children, home-tools, home-rail, treatment-wrap, page-card)

### JS
- `setActiveSlide`: reads `deck.scrollTop` / `clientHeight`; writes `--p` & `--abs-p` per slide for live parallax
- `goToSlide`: uses `{ top: index * clientHeight }` instead of `left`
- Removed wheel hijack that translated deltaY → scrollLeft (natural vertical scroll now)

## Verified
- Headless Playwright test confirmed: deck overflow-y auto / x hidden, snap y mandatory, slides stacked vertically (scrollHeight = 9 × viewport), active class toggles correctly on scroll, CSS progress vars update in real time.
- All original content (home slide, 8 treatment slides, package boxes, videos, CTAs, rail, phase2/3/4 dynamic additions) intact.

## Next Action Items
- User pushes changes back to GitHub repo via "Save to Github" feature in the chat (platform can't push directly)
- Optional tuning: parallax intensity, animation durations, easing, stagger delays

## Future / Backlog
- Reduced-motion media query to disable 3D transforms for accessibility
- Per-slide custom reveal variants (scale-in vs slide-in) for variety
