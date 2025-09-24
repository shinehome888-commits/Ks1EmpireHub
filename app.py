import streamlit as st
import os

# ------------------- CONFIG -------------------
PROJECTS = {
    "ShineGPT": {
        "name": "ShineGPT",
        "desc": "Learn AI, Blockchain, Web3 — offline. No internet needed.",
        "link": "/shinegpt",
        "icon": "🤖"
    },
    "Panda": {
        "name": "Panda",
        "desc": "Sell your NFT art — 0% fees. Earn in HOPE Coin.",
        "link": "/panda",
        "icon": "🐼"
    },
    "Sarah": {
        "name": "Sarah",
        "desc": "NFT tickets for events — concerts, workshops, village meetings.",
        "link": "/sarah",
        "icon": "🎫"
    },
    "Welee": {
        "name": "Welee",
        "desc": "Vote on community projects — school wells, solar lights, policies.",
        "link": "/welee",
        "icon": "🗳️"
    },
    "Owen": {
        "name": "Owen",
        "desc": "Buy, sell, or lease land — tokenized on blockchain.",
        "link": "/owen",
        "icon": "🏡"
    },
    "Sobahboy": {
        "name": "Sobahboy",
        "desc": "Upload your music. Sell it as NFT. Keep 100% of royalties.",
        "link": "/sobahboy",
        "icon": "🎵"
    },
    "Gbarku": {
        "name": "Gbarku",
        "desc": "Traditional African art. Digitized. Owned. Sold.",
        "link": "/gbarku",
        "icon": "🎨"
    },
    "Pinko": {
        "name": "Pinko",
        "desc": "Live tracker: Crypto, NFTs, DeFi, Metaverse, DAOs, IoT.",
        "link": "/pinko",
        "icon": "📈"
    },
    "Riji": {
        "name": "Riji",
        "desc": "2D Metaverse — walk into Gbarku, join Welee, listen to podcasts.",
        "link": "/riji",
        "icon": "🌐"
    },
    "Hannah": {
        "name": "Hannah",
        "desc": "Create your own DAO — govern your village, church, or coop.",
        "link": "/hannah",
        "icon": "🤝"
    },
    "HopeCoin": {
        "name": "HOPE Coin",
        "desc": "Earn it. Spend it. Own it. Your token. Your power.",
        "link": "/hope",
        "icon": "🪙"
    },
    "Sobah": {
        "name": "Sobah",
        "desc": "Your digital wallet. Send HOPE Coin. No bank. No fees.",
        "link": "/sobah",
        "icon": "🏦"
    },
    "Teah": {
        "name": "Teah",
        "desc": "Lend or borrow HOPE Coin — no credit check. No middleman.",
        "link": "/teah",
        "icon": "💸"
    },
    "Jones": {
        "name": "Jones",
        "desc": "Sell your goods — food, crafts, tools — for HOPE Coin.",
        "link": "/jones",
        "icon": "🛒"
    },
    "MaTettee": {
        "name": "Ma Tettee",
        "desc": "Post. Share. Earn. No ads. No tracking. Just community.",
        "link": "/matettee",
        "icon": "📱"
    },
    "RedButterflies": {
        "name": "RedButterflies",
        "desc": "Adult creators — own your content. No censorship.",
        "link": "/redbutterflies",
        "icon": "🦋"
    },
    "Dylan": {
        "name": "Dylan",
        "desc": "Upload videos. Sell access. Earn HOPE Coin.",
        "link": "/dylan",
        "icon": "🎥"
    },
    "FeeFee": {
        "name": "FeeFee",
        "desc": "Podcasts, folktales, proverbs — sold as NFTs.",
        "link": "/feefee",
        "icon": "🎙️"
    },
    "KS1NFT": {
        "name": "KS1 NFT Collection",
        "desc": "Own a piece of the empire. Membership NFTs for learners.",
        "link": "/ks1nft",
        "icon": "👑"
    },
    "William": {
        "name": "William",
        "desc": "Fans-only NFT platform — exclusive access for supporters.",
        "link": "/william",
        "icon": "🌟"
    },
    "KS1Podcast": {
        "name": "The KS1 Podcast",
        "desc": "Stories from elders. Lessons from the future.",
        "link": "/podcast",
        "icon": "📻"
    },
    "Michael": {
        "name": "Michael",
        "desc": "Decentralized exchange — trade crypto, no KYC, no gate.",
        "link": "/michael",
        "icon": "🔄"
    }
}

# ------------------- PAGE NAVIGATION -------------------
def show_home():
    st.markdown("<h1 style='text-align: center; color: #D4AF37;'>KS1 EMPIRE HUB</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #ffffff;'>One Door. One Login. One Future.</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #ffffff; margin-bottom: 40px;'>Powered by KS1 Empire Foundation</h4>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; color: #e0e0e0; font-size: 1.2rem; margin-bottom: 50px;'>No bank. No ID. No internet? No problem. Learn. Earn. Own.</p>", unsafe_allow_html=True)

    cols = st.columns(4)
    i = 0
    for key, project in PROJECTS.items():
        with cols[i % 4]:
            st.markdown(f"<div style='text-align: center; padding: 15px; border-radius: 12px; background-color: #111111; margin: 10px; border: 1px solid #D4AF37;'>"
                        f"<h3 style='color: #D4AF37;'>{project['icon']}</h3>"
                        f"<h4 style='color: #ffffff; margin: 5px 0;'>{project['name']}</h4>"
                        f"<p style='color: #e0e0e0; font-size: 0.9rem;'>{project['desc']}</p>"
                        "</div>", unsafe_allow_html=True)
            if st.button(f"Open {project['name']}", key=key):
                st.session_state.page = project['link']
                st.rerun()
        i += 1

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #D32F2F; font-size: 1.1rem;'><strong>Free. Open. Forever.</strong></p>", unsafe_allow_html=True)

def show_project_page(project_key):
    project = PROJECTS[project_key]
    st.markdown(f"<h1 style='text-align: center; color: #D4AF37;'>{project['icon']} {project['name']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center; color: #ffffff;'>{project['desc']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #e0e0e0; font-size: 1.1rem;'>Coming soon — built by KS1 Empire Foundation.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #ffffff; font-size: 0.9rem;'>This project is under development. Check back soon.</p>", unsafe_allow_html=True)
    st.markdown("---")
    if st.button("← Back to Home"):
        st.session_state.page = "/"
        st.rerun()

# ------------------- MAIN APP -------------------
st.set_page_config(page_title="KS1 Empire Hub", page_icon="👑", layout="centered")

if 'page' not in st.session_state:
    st.session_state.page = "/"

if st.session_state.page == "/":
    show_home()
else:
    # Find project key by link
    for key, project in PROJECTS.items():
        if st.session_state.page == project['link']:
            show_project_page(key)
            break
    else:
        st.session_state.page = "/"
        st.rerun()
