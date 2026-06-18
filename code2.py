import streamlit as st

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Bring Hats",
    page_icon="🧢",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  GLOBAL CSS  (drip font + dark streetwear theme)
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Rubik:wght@400;700&display=swap');

/* ── base ── */
html, body, [class*="css"] {
    background-color: #0a0a0a !important;
    color: #f0f0f0 !important;
    font-family: 'Rubik', sans-serif;
}

/* ── drip title ── */
.drip-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(3.5rem, 9vw, 7rem);
    letter-spacing: 0.12em;
    text-align: center;
    line-height: 1;
    background: linear-gradient(180deg, #ffffff 0%, #d4af37 40%, #a0830f 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    /* drip drop-shadow simulation */
    filter: drop-shadow(0 4px 0 #d4af37) drop-shadow(0 8px 0 #8a6300)
            drop-shadow(0 12px 6px rgba(212,175,55,0.35));
    margin-bottom: 0;
}

.drip-sub {
    text-align: center;
    color: #888;
    font-size: 0.95rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    margin-top: 0.25rem;
    margin-bottom: 2rem;
}

/* ── brand nav buttons ── */
div[data-testid="column"] > div > div > div > button {
    width: 100%;
}

.brand-btn {
    display: block;
    width: 100%;
    padding: 0.75rem 1rem;
    margin: 0.3rem 0;
    border: 2px solid #2a2a2a;
    border-radius: 8px;
    background: #111;
    color: #f0f0f0;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.3rem;
    letter-spacing: 0.1em;
    cursor: pointer;
    transition: border-color 0.2s, background 0.2s;
    text-align: center;
}
.brand-btn:hover { border-color: #d4af37; background: #1a1a1a; }
.brand-btn.active { border-color: #d4af37; background: #1c1600; color: #d4af37; }

/* ── section header ── */
.section-header {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.4rem;
    letter-spacing: 0.15em;
    color: #d4af37;
    border-bottom: 2px solid #2a2a2a;
    padding-bottom: 0.4rem;
    margin-bottom: 1.5rem;
}

/* ── product card ── */
.hat-card {
    background: #111;
    border: 1px solid #222;
    border-radius: 12px;
    padding: 1rem;
    margin-bottom: 1rem;
    transition: border-color 0.2s, transform 0.2s;
    height: 100%;
}
.hat-card:hover {
    border-color: #d4af37;
    transform: translateY(-3px);
}
.hat-emoji {
    font-size: 3.5rem;
    text-align: center;
    display: block;
    margin-bottom: 0.6rem;
}
.hat-name {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.15rem;
    letter-spacing: 0.08em;
    color: #ffffff;
    text-align: center;
    margin-bottom: 0.2rem;
}
.hat-brand-tag {
    text-align: center;
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #d4af37;
    margin-bottom: 0.5rem;
}
.hat-price {
    text-align: center;
    font-size: 1.2rem;
    font-weight: 700;
    color: #f0f0f0;
    margin-bottom: 0.6rem;
}
.hat-colors {
    display: flex;
    gap: 5px;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 0.7rem;
}
.color-dot {
    width: 14px; height: 14px;
    border-radius: 50%;
    border: 1.5px solid #333;
    display: inline-block;
}

/* ── cart badge ── */
.cart-badge {
    background: #d4af37;
    color: #000;
    border-radius: 50%;
    padding: 0.1rem 0.5rem;
    font-weight: 700;
    font-size: 0.85rem;
}

/* ── divider ── */
hr { border-color: #1e1e1e !important; }

/* ── hide streamlit chrome ── */
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: #0a0a0a; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  CATALOG DATA
# ─────────────────────────────────────────────
CATALOG = {
    "Barbas": [
        {"name": "Barbas Classic Logo", "price": 350, "colors": ["#1a1a1a","#ffffff","#8b4513"], "emoji": "🧢"},
        {"name": "Barbas Vintage Wash", "price": 380, "colors": ["#4a3728","#c8b89a","#2c2c2c"], "emoji": "🧢"},
        {"name": "Barbas Snapback OG", "price": 420, "colors": ["#000000","#d4af37","#8b0000"], "emoji": "🧢"},
        {"name": "Barbas Trucker Mesh", "price": 320, "colors": ["#f5f5dc","#1a1a1a","#556b2f"], "emoji": "🧢"},
        {"name": "Barbas Low Profile", "price": 360, "colors": ["#2f4f4f","#dcdcdc","#8b4513"], "emoji": "🧢"},
        {"name": "Barbas Dad Hat Corduroy", "price": 390, "colors": ["#8b4513","#d2691e","#000000"], "emoji": "🧢"},
        {"name": "Barbas 5-Panel Camp", "price": 340, "colors": ["#556b2f","#f5deb3","#2f4f4f"], "emoji": "🧢"},
        {"name": "Barbas Fitted Pro", "price": 450, "colors": ["#000080","#c0c0c0","#000000"], "emoji": "🧢"},
        {"name": "Barbas Camo Drop", "price": 410, "colors": ["#4b5320","#78866b","#8b7355"], "emoji": "🧢"},
        {"name": "Barbas Embroidered Rose", "price": 440, "colors": ["#1c1c1c","#8b0000","#f5f5dc"], "emoji": "🧢"},
    ],
    "Hats": [
        {"name": "Hats Co. Bucket Linen", "price": 310, "colors": ["#f5f5dc","#d2b48c","#fff8dc"], "emoji": "🪖"},
        {"name": "Hats Co. Boonie Wide Brim", "price": 370, "colors": ["#6b8e23","#8b7355","#2e2e2e"], "emoji": "🪖"},
        {"name": "Hats Co. Flex Fitted", "price": 400, "colors": ["#000000","#ffffff","#c0c0c0"], "emoji": "🧢"},
        {"name": "Hats Co. Flat Bill Snap", "price": 430, "colors": ["#191970","#d4af37","#ff4500"], "emoji": "🧢"},
        {"name": "Hats Co. Straw Panama", "price": 480, "colors": ["#d2b48c","#8b6914","#f5deb3"], "emoji": "👒"},
        {"name": "Hats Co. Beanie Knit", "price": 290, "colors": ["#1a1a1a","#8b0000","#2f4f4f"], "emoji": "🧣"},
        {"name": "Hats Co. Trucker Foam", "price": 350, "colors": ["#ffffff","#1a1a1a","#ff6347"], "emoji": "🧢"},
        {"name": "Hats Co. Military Cap", "price": 420, "colors": ["#4b5320","#1a1a1a","#8b7355"], "emoji": "🧢"},
        {"name": "Hats Co. Leather Strap", "price": 500, "colors": ["#4a2c0a","#1a1a1a","#c0a060"], "emoji": "🧢"},
        {"name": "Hats Co. Neon Strike", "price": 360, "colors": ["#000000","#39ff14","#ff073a"], "emoji": "🧢"},
    ],
    "Dandy": [
        {"name": "Dandy Fedora Classic", "price": 520, "colors": ["#2c2c2c","#d4af37","#8b7355"], "emoji": "🎩"},
        {"name": "Dandy Wide Brim Felt", "price": 580, "colors": ["#1a1a1a","#c8a96e","#4a4a4a"], "emoji": "🎩"},
        {"name": "Dandy Pork Pie", "price": 490, "colors": ["#2f2f2f","#d2b48c","#8b0000"], "emoji": "🎩"},
        {"name": "Dandy Trilby Wool", "price": 540, "colors": ["#3b3b3b","#f5deb3","#556b2f"], "emoji": "🎩"},
        {"name": "Dandy Straw Fedora", "price": 470, "colors": ["#d2b48c","#8b6914","#2c2c2c"], "emoji": "👒"},
        {"name": "Dandy Flat Cap Tweed", "price": 430, "colors": ["#6b5b45","#c8b89a","#2c3e50"], "emoji": "🎩"},
        {"name": "Dandy Cowboy Suede", "price": 620, "colors": ["#8b4513","#d2691e","#f5deb3"], "emoji": "🤠"},
        {"name": "Dandy Boater Summer", "price": 460, "colors": ["#f5f5dc","#1a1a1a","#ff6347"], "emoji": "👒"},
        {"name": "Dandy Top Hat Silk", "price": 750, "colors": ["#0a0a0a","#c0c0c0","#d4af37"], "emoji": "🎩"},
        {"name": "Dandy Gatsby Newsboy", "price": 500, "colors": ["#4a3728","#d2b48c","#1a1a1a"], "emoji": "🎩"},
    ],
    "31 Hats": [
        {"name": "31 Original Snapback", "price": 380, "colors": ["#000000","#d4af37","#ffffff"], "emoji": "🧢"},
        {"name": "31 OG Fitted Black", "price": 420, "colors": ["#1a1a1a","#c0c0c0","#8b0000"], "emoji": "🧢"},
        {"name": "31 Trucker Classic", "price": 340, "colors": ["#ffffff","#1a1a1a","#d4af37"], "emoji": "🧢"},
        {"name": "31 5-Panel White", "price": 310, "colors": ["#f5f5f5","#1a1a1a","#ff073a"], "emoji": "🧢"},
        {"name": "31 Camo Drop Vol.1", "price": 400, "colors": ["#4b5320","#78866b","#d4af37"], "emoji": "🧢"},
        {"name": "31 Vintage Dad Hat", "price": 360, "colors": ["#c8b89a","#4a3728","#2c2c2c"], "emoji": "🧢"},
        {"name": "31 Corduroy Navy", "price": 390, "colors": ["#000080","#d4af37","#c0c0c0"], "emoji": "🧢"},
        {"name": "31 Mesh Back Fire", "price": 330, "colors": ["#ff4500","#1a1a1a","#f5f5f5"], "emoji": "🧢"},
        {"name": "31 Chenille Patch", "price": 450, "colors": ["#2c2c2c","#8b0000","#d4af37"], "emoji": "🧢"},
        {"name": "31 Wool Blend", "price": 480, "colors": ["#1a1a1a","#c8c8c8","#8b4513"], "emoji": "🧢"},
        {"name": "31 Summer Straw", "price": 350, "colors": ["#d2b48c","#8b6914","#ffffff"], "emoji": "👒"},
        {"name": "31 Neon Nights", "price": 370, "colors": ["#000000","#39ff14","#ff00ff"], "emoji": "🧢"},
        {"name": "31 Leather Patch Pro", "price": 520, "colors": ["#1a1a1a","#8b4513","#d4af37"], "emoji": "🧢"},
        {"name": "31 Flag Series", "price": 395, "colors": ["#c8102e","#ffffff","#012169"], "emoji": "🧢"},
        {"name": "31 Graff Edition", "price": 430, "colors": ["#000000","#ff073a","#39ff14"], "emoji": "🧢"},
    ],
}

# ─────────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────────
if "brand" not in st.session_state:
    st.session_state.brand = "Barbas"
if "cart" not in st.session_state:
    st.session_state.cart = []
if "search" not in st.session_state:
    st.session_state.search = ""

# ─────────────────────────────────────────────
#  HEADER — drip title
# ─────────────────────────────────────────────
st.markdown("""
<div style="padding: 2rem 0 0.5rem 0;">
  <div class="drip-title">BRING HATS</div>
  <div class="drip-sub">🧢 &nbsp; Tu tienda de gorras premium &nbsp; 🧢</div>
</div>
""", unsafe_allow_html=True)

# cart count in top-right
total_items = len(st.session_state.cart)
col_space, col_cart = st.columns([9, 1])
with col_cart:
    if st.button(f"🛒 {total_items}", key="cart_btn", help="Ver carrito"):
        st.session_state.brand = "__cart__"

st.markdown("<hr>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  BRAND NAV
# ─────────────────────────────────────────────
brands = list(CATALOG.keys())
nav_cols = st.columns(len(brands))
for i, b in enumerate(brands):
    with nav_cols[i]:
        active_style = "background:#1c1600;border-color:#d4af37;color:#d4af37;" if st.session_state.brand == b else ""
        if st.button(b, key=f"nav_{b}", use_container_width=True):
            st.session_state.brand = b

# ─────────────────────────────────────────────
#  SEARCH
# ─────────────────────────────────────────────
search_query = st.text_input(
    "", placeholder="🔍  Busca tu gorra...",
    key="search_input",
    label_visibility="collapsed"
)

st.markdown("<hr>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  CART VIEW
# ─────────────────────────────────────────────
def show_cart():
    st.markdown('<div class="section-header">🛒 Tu Carrito</div>', unsafe_allow_html=True)
    if not st.session_state.cart:
        st.info("Tu carrito está vacío. ¡Agrega gorras al carrito!")
        return
    total = 0
    for idx, item in enumerate(st.session_state.cart):
        c1, c2, c3 = st.columns([5, 2, 1])
        with c1:
            st.write(f"{item['emoji']} **{item['name']}** — *{item['brand']}*")
        with c2:
            st.write(f"${item['price']:,}")
        with c3:
            if st.button("✕", key=f"rm_{idx}"):
                st.session_state.cart.pop(idx)
                st.rerun()
        total += item["price"]
        st.divider()
    st.markdown(f"### Total: **${total:,} MXN**")
    if st.button("✅ Confirmar Pedido", use_container_width=True):
        st.balloons()
        st.success("¡Pedido confirmado! Pronto nos ponemos en contacto contigo. 🎉")
        st.session_state.cart = []

# ─────────────────────────────────────────────
#  PRODUCT GRID
# ─────────────────────────────────────────────
def color_dots(colors):
    dots = "".join(
        f'<span class="color-dot" style="background:{c};"></span>'
        for c in colors
    )
    return f'<div class="hat-colors">{dots}</div>'

def show_catalog(brand_name, items, query=""):
    st.markdown(f'<div class="section-header">{brand_name}</div>', unsafe_allow_html=True)
    filtered = [h for h in items if query.lower() in h["name"].lower()] if query else items

    if not filtered:
        st.warning("No se encontraron gorras con ese término.")
        return

    cols_per_row = 4
    rows = [filtered[i:i+cols_per_row] for i in range(0, len(filtered), cols_per_row)]

    for row in rows:
        cols = st.columns(cols_per_row)
        for j, hat in enumerate(row):
            with cols[j]:
                st.markdown(f"""
                <div class="hat-card">
                  <span class="hat-emoji">{hat['emoji']}</span>
                  <div class="hat-name">{hat['name']}</div>
                  <div class="hat-brand-tag">{brand_name}</div>
                  <div class="hat-price">${hat['price']:,} MXN</div>
                  {color_dots(hat['colors'])}
                </div>
                """, unsafe_allow_html=True)
                if st.button("Agregar al carrito", key=f"add_{brand_name}_{hat['name']}", use_container_width=True):
                    st.session_state.cart.append({**hat, "brand": brand_name})
                    st.toast(f"✅ {hat['name']} agregada al carrito")

# ─────────────────────────────────────────────
#  MAIN RENDER
# ─────────────────────────────────────────────
if st.session_state.brand == "__cart__":
    show_cart()
elif search_query:
    # search across all brands
    st.markdown('<div class="section-header">🔍 Resultados de búsqueda</div>', unsafe_allow_html=True)
    found_any = False
    for brand_name, items in CATALOG.items():
        results = [h for h in items if search_query.lower() in h["name"].lower()]
        if results:
            show_catalog(brand_name, results)
            found_any = True
    if not found_any:
        st.warning("No se encontraron gorras. Intenta con otro término.")
else:
    brand = st.session_state.brand
    show_catalog(brand, CATALOG[brand])

# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; color:#444; font-size:0.8rem; padding: 1rem 0 2rem 0; letter-spacing:0.2em;">
  BRING HATS © 2025 &nbsp;·&nbsp; BARBAS · HATS · DANDY · 31 HATS &nbsp;·&nbsp; HECHO CON 🧢
</div>
""", unsafe_allow_html=True)
