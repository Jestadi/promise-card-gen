import streamlit as st
import random

from PIL import Image
image = Image.open("img/Group 6.png")
st.image(image, use_column_width=True)
st.title("Promise Generator for 2023")
st.subheader("Happy New Year!")
verse_num = dict({
    "Deuteronomy 31:8":"The LORD himself goes before you and will be with you he will never leave you nor forsake you. Do not be afraid; do not be discouraged.",
    "Romans 15:13":"May the God of hope fill you with all joy and peace as you trust in him, so that you may overflow with hope by the power of the Holy Spirit.",
    "Joshua 1:9":"Have I not commanded you? Be strong and courageous. Do not be afraid; do not be discouraged, for the LORD your God will be with you wherever you go.",
    "Matthew 11:28-29":"Come to me, all you who are weary and burdened, and I will give you rest. Take my yoke upon you and learn from me, for I am gentle and humble in heart, and you will find rest for your souls.",
    "Psalm 37:4":"Delight yourself in the Lord, and he will give you the desires of your heart.",
    "Mark 11:24":"Therefore I tell you, whatever you ask in prayer, believe that you have received it, and it will be yours.",
    "Isaiah 55:12":"For you shall go out in joy and be led forth in peace; the mountains and the hills before you shall break forth into singing, and all the trees of the field shall clap their hands.",
    "Jeremiah 29:11":"'For I know the plans I have for you', declares the Lord, 'plans to prosper you and not to harm you, plans to give you hope and a future'",
    "Deuteronomy 31:6":" Be strong and courageous. Do not fear or be in dread of them, for it is the Lord your God who goes with you. He will not leave you or forsake you.",
    "Isaiah 41:10":"So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand.",
    "Isaiah 43:2":"When you pass through the waters, I will be with you; and when you pass through the rivers, they will not sweep over you. When you walk through the fire, you will not be burned; the flames will not set you ablaze.",
    "Isaiah 41:13":"For I am the LORD your God who takes hold of your right hand and says to you, Do not fear; I will help you.",
    "Deuteronomy 11:13,14":"And it shall be that if you earnestly obey My commandments which I command you today, to love the Lord your God and serve Him with all your heart and with all your soul, then I will give you the rain in its season, the early rain and the latter rain, that you may gather in your grain, your new wine, and your oil",
    "Psalm 121:3":"He will not allow your foot to be moved; He who keeps you will not slumber",
    "Lamentations 3:22,23":"Through the Lord's mercies we are not consumed, Because His compassions fail not. They are new every morning; Great is your faithfulness",
    "Jeremiah 32:40":"And I will make an everlasting covenant with them, that I will never turn away from doing them good; but I will put my fear in their hearts so they will not depart from me.",
    "Deuteronomy 1:30":"The Lord your God, who goes before you, He will fight for you, according to all He did for you in Egypt before your eyes.",
    "Psalm 55:22":"Cast your burdens on the Lord, and He shall sustain you. He shall never permit the righteous to be moved.",
    "Psalm 48:14":"For this is God, Our God forever and ever; He will be our guide even to death",
    "Isaiah 64:4":"For since the beginning of the world, Men have not heard nor perceived by the ear, nor has the eye seen any God besides You, Who acts for the one who waits for Him.",
    "Hebrews 13:5":"Let your conduct be without covetousness; be content with such things as you have. For He Himself has said, 'I will never leave you nor forsake you'",
    "Proverbs 16:3":"Commit your works to the LORD, and your thoughts will be established",
    "2 Samuel 22:33,34":"God is my strength and power, and He makes my way perfect. He makes my feet like the feet of a deer, and sets me on my high places.",
    "Jeremiah 24:6":"For I will set my eyes on them for good, and I will bring them back to this land; I will build them and not pull them down, and I will plant them and not pluck them up.",
    "Deuteronomy 33:12":"The beloved of the Lord shall dwell in safety by Him, who shelters him all the day long; and He shall dwell between His shoulders.",
    "Luke 12:31":"But seek the kingdom of God, and all these things shall be added to you.",
    "Phillipians 4:13":"I can do all things through Christ who strengthens me.",
    "1 Corinthians 2:9":"Eye has not seen, nor ear heard, nor have entered into the heart of man, the things which God has prepared for those who love Him.",
    "Ephesians 3:20":"Now to Him who is able to do exceedingly abundantly above all that we ask or think, according to the power that works in us, to Him be glory in the church by Christ Jesus to all generations.",
    "Isaiah 58:7,8":"Is it not to share your bread with the hungry, and that you bring to your house the poor who are cast out; when you see the naked, that you cover him, and not hide from your own flesh: Then your light shall break forth like the morning, your healing shall spring forth speedily, and your righteousness shall go before you, the glory of the Lord shall be your rear guard.",
    "Habakkuk 3:19":"The Lord God is my strength; He will make my feet like deer's feet, and He will make me walk on my high hills",
    "Psalm 86:7":"In the day of my trouble I will call upon You, for you will answer me.",
    "Ephesians 6:11":"Put on the whole armor of God, that you may be able to stand against the wiles of the devil.",
    "1 John 4:18":"There is no fear in love; but perfect love casts out fear, because fear involves torment. But he who fears has not been made perfect in love. "
    })

selected_app_mode = st.session_state.get('app_mode')

st.write("Please enter your name below")
name = st.text_input("Type Here ...")
 
# display the name when the submit button is clicked
# .title() is used to get the input text string

if(st.button('Submit')):
    result = name.title()

st.write("Once you submit name, simply click 'My promise' button below to get your 2023 promise verse")

key,value = random.choice(list(verse_num.items()))

if(st.button("My promise")):

    st.text("Here's your promise for this year, {}.".format(name))
    st.subheader(key)
    st.write(value)
      



