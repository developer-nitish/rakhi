import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io
from textwrap import wrap

# Page configuration for a nice title and icon
st.set_page_config(
    page_title="Modern Raksha Bandhan",
    page_icon="✨",
    layout="wide"
)

# --- CSS for a modern, animated look ---
def apply_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    body {
        font-family: 'Poppins', sans-serif;
    }
    .main-header {
        text-align: center;
        background: -webkit-linear-gradient(45deg, #ff69b4, #8a2be2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 600;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #555;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #ff69b4;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 24px;
        font-size: 18px;
        font-weight: 600;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    .stDownloadButton>button {
        background-color: #8a2be2;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 24px;
        font-size: 18px;
        font-weight: 600;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stDownloadButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    .glass-card-bg {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 16px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 20px;
    }
    .stApp {
        background: linear-gradient(45deg, #f0e4d7, #e6c8e0, #a0d4ef);
        background-size: 400% 400%;
        animation: gradient-animation 15s ease infinite;
    }
    @keyframes gradient-animation {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .st-emotion-cache-121p9e6 {
      border-radius: 12px;
      padding: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Function to create the styled Rakhi Card ---
def create_modern_card(rakhi_text, sibling_name, uploaded_photo=None):
    """
    Glassmorphism effect ke sath ek modern Rakhi card banata hai PIL ka upyog karke.
    """
    try:
        title_font = ImageFont.truetype("arial.ttf", 45)
        message_font = ImageFont.truetype("arial.ttf", 20)
        name_font = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        st.warning("Font file nahi mila. Default font ka upyog kiya ja raha hai.")
        title_font = ImageFont.load_default()
        message_font = ImageFont.load_default()
        name_font = ImageFont.load_default()
    
    img_width, img_height = 900, 600
    final_image = Image.new('RGB', (img_width, img_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(final_image)

    card_width, card_height = 650, 450
    card_x = (img_width - card_width) // 2
    card_y = (img_height - card_height) // 2
    
    # Glassmorphism effect ke liye ek semitransparent layer banayein
    glass_overlay = Image.new('RGBA', (img_width, img_height), (255, 255, 255, 128))
    glass_overlay.paste(Image.new('RGB', (card_width, card_height), 'white'), (card_x, card_y))
    glass_overlay = glass_overlay.filter(ImageFilter.GaussianBlur(10))
    
    final_image.paste(glass_overlay, (0, 0), glass_overlay)

    # Beech mein card ka content
    draw.rectangle([card_x, card_y, card_x + card_width, card_y + card_height], fill=(255, 255, 255, 128))
    
    # Text
    draw.text((card_x + 40, card_y + 30), "Happy Raksha Bandhan!", fill='black', font=title_font)
    
    wrapped_text = "\n".join(wrap(rakhi_text, width=55))
    draw.text((card_x + 40, card_y + 100), wrapped_text, fill='black', font=message_font)
    
    if sibling_name:
        name_text = f"From: {sibling_name}"
        draw.text((card_x + 40, card_y + card_height - 60), name_text, fill='black', font=name_font)

    if uploaded_photo:
        uploaded_image = Image.open(uploaded_photo).convert("RGB")
        photo_size = (150, 150)
        uploaded_image = uploaded_image.resize(photo_size, Image.Resampling.LANCZOS)
        
        photo_x = card_x + card_width - photo_size[0] - 30
        photo_y = card_y + 30
        final_image.paste(uploaded_image, (photo_x, photo_y))
    
    return final_image

# --- Main Streamlit App ---
apply_custom_css()

st.markdown('<h1 class="main-header">Digital Raksha Bandhan 💖</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">एक अनोखे अंदाज़ में रिश्तों का जश्न मनाएं</p>', unsafe_allow_html=True)

# --- 1. Design Your Rakhi ---
st.header("1. अपनी डिजिटल राखी डिजाइन करें")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("अपनी राखी को अनुकूलित करें")
    
    sibling_name = st.text_input('कार्ड पर अपना नाम लिखें', 'आपका भाई/बहन')
    
    rakhi_text = st.text_area('अपने भाई या बहन के लिए एक व्यक्तिगत संदेश लिखें',
                               "Behen, tum meri life ka Wi-Fi ho -- hamesha connected rakhti ho, kabhi kabhi irritate karti ho, par tumhare bina life ka signal hi chala jata hai. Happy Raksha Bandhan! Tum meri hamesha wali 'Best Partner in Crime' rahogi.💖",
                               height=150)

    uploaded_photo = st.file_uploader("अपने भाई या बहन की एक फोटो अपलोड करें", type=["jpg", "png", "jpeg"])
    
    if uploaded_photo:
        st.success("फोटो सफलतापूर्वक अपलोड हो गई! 🎉")

with col2:
    st.subheader("आपकी राखी का प्रीव्यू")
    
    # Card preview
    card_image = create_modern_card(rakhi_text, sibling_name, uploaded_photo)
    st.image(card_image, caption="आपका व्यक्तिगत राखी कार्ड", use_column_width=True)

    img_byte_arr = io.BytesIO()
    card_image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    st.download_button(
        label="राखी कार्ड डाउनलोड करें 🖼️",
        data=img_byte_arr,
        file_name="my_digital_rakhi.png",
        mime="image/png",
        use_container_width=True
    )
    st.info("आपका कार्ड साझा करने के लिए तैयार है! इसे डाउनलोड करने के लिए ऊपर दिए गए बटन पर क्लिक करें।")
    
# --- 2. Share a Rakhi Story ---
st.markdown("---")
st.header("2. राखी की कहानी साझा करें")

with st.expander("कहानी बताने के लिए यहाँ क्लिक करें"):
    story_prompt = st.text_area("अपने भाई या बहन के साथ अपने सबसे यादगार पल के बारे में बताएं...", height=150)

    if st.button("AI कहानी बनाएं"):
        if story_prompt:
            with st.spinner('AI आपके लिए एक सुंदर कहानी बुन रहा है... ⏳'):
                import time
                time.sleep(3)
            
            st.success("आपकी कहानी AI द्वारा बनाई गई है! 🎉")
            st.markdown(f"**आपकी याद के आधार पर:**\n\n> *\"{story_prompt}\"*")
            st.markdown("---")
            st.write("*(यह वह जगह है जहाँ आपकी AI द्वारा बनाई गई कहानी दिखाई देगी।)*")
            st.markdown("---")
        else:
            st.error("कहानी बनाने के लिए कृपया एक याद लिखें।")
            
st.markdown("---")

# --- Footer ---
st.markdown("Made with ❤️ for all the brothers and sisters around the world.")
