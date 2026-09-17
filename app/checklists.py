<<<<<<< HEAD
"""What to check before buying in person at the shop.

GEBEYA TECH is a broker service. Every item listed is available for
inspection and purchase at partner shops in Bole, Edna Mall.
"""

# =====================================================
# OUR PROMISE
# =====================================================

PROMISE = {
    "en": [
        {"icon": "✅", "title": "Real photos", "body": "The photos on the website are the actual item."},
        {"icon": "✅", "title": "Honest specs", "body": "Battery health, condition, storage — everything is written truthfully."},
        {"icon": "✅", "title": "Fair pricing", "body": "Our prices match the current Addis market. No inflated numbers."},
        {"icon": "✅", "title": "Pay at the shop, after you check", "body": "You pay the shop directly, only after you're satisfied."},
        {"icon": "✅", "title": "No deposit, no pressure", "body": "Message us to arrange viewing. Walk away if it's not right."},
    ],
    "am": [
        {"icon": "✅", "title": "እውነተኛ ፎቶዎች", "body": "በድረ-ገጹ ላይ ያሉት ፎቶዎች ትክክለኛውን ዕቃ ያሳያሉ።"},
        {"icon": "✅", "title": "ታማኝ ዝርዝር", "body": "የባትሪ ጤንነት፣ ሁኔታ፣ ማከማቻ — ሁሉም በእውነት ተጽፏል።"},
        {"icon": "✅", "title": "ተመጣጣኝ ዋጋ", "body": "ዋጋዎቻችን ከአዲስ አበባ ገበያ ጋር ይመሳሰላሉ።"},
        {"icon": "✅", "title": "በሱቁ ይክፈሉ፣ ካረጋገጡ በኋላ", "body": "ዕቃውን ካረኩ በኋላ ብቻ ለሱቁ በቀጥታ ይክፈሉ።"},
        {"icon": "✅", "title": "ቅድሚያ ክፍያ የለም", "body": "ለመመልከት ያግኙን። ዕቃው የማይስማማ ከሆነ ይራመዱ።"},
    ],
}

# =====================================================
# CATEGORY CHECKLISTS
# =====================================================

CHECKLISTS = {
    "phones": {
        "en": {
            "title": "📱 Before you buy this phone",
            "subtitle": "Ask the seller to show you these things at the shop",
            "sections": [
                {"heading": "IMEI check", "items": [
                    "Dial *#06# — the IMEI on screen matches the box",
                    "IMEI is exactly 15 digits",
                    "IMEI matches what's on this listing",
                ]},
                {"heading": "Battery", "items": [
                    "Battery health matches what's listed",
                    "Ask to plug it in — does it charge?",
                    "Feel the back — is it warm (shouldn't be)",
                ]},
                {"heading": "Screen", "items": [
                    "No cracks or dead pixels",
                    "Touch responds everywhere",
                    "Brightness adjusts normally",
                ]},
                {"heading": "Functions", "items": [
                    "Front and back cameras work",
                    "Speaker plays clear sound",
                    "Microphone records",
                    "Both SIM slots work",
                    "Wi-Fi, Bluetooth, GPS work",
                    "Face ID or fingerprint works",
                    "Power and volume buttons work",
                ]},
                {"heading": "Before you pay", "items": [
                    "Price matches what's on the website",
                    "You've tested everything above",
                    "You're satisfied with the condition",
                ]},
            ],
        },
        "am": {
            "title": "📱 ይህን ስልክ ከመግዛትዎ በፊት",
            "subtitle": "በሱቁ ውስጥ እነዚህን እንዲያሳይዎ ሻጩን ይጠይቁ",
            "sections": [
                {"heading": "IMEI ማረጋገጫ", "items": [
                    "*#06# ይደውሉ — በስክሪኑ ላይ ያለው IMEI ከሳጥኑ ጋር ይመሳሰላል",
                    "IMEI በትክክል 15 አሃዞች ነው",
                    "IMEI በዚህ ዝርዝር ላይ ካለው ጋር ይመሳሰላል",
                ]},
                {"heading": "ባትሪ", "items": [
                    "የባትሪ ጤንነት ከተጠቀሰው ጋር ይመሳሰላል",
                    "እንዲሰካ ይጠይቁ — ይሞላል?",
                    "የኋላውን ይንኩ — ሞቅ ብሎ መሆን የለበትም",
                ]},
                {"heading": "ስክሪን", "items": [
                    "ስንጥቅ ወይም የሞቱ ፒክሴሎች የሉም",
                    "በሁሉም ቦታ ይነካል",
                    "የብሩህነት መጠን በተለምዶ ይቀያየራል",
                ]},
                {"heading": "ተግባራት", "items": [
                    "የፊት እና የኋላ ካሜራዎች ይሰራሉ",
                    "ስፒከር ግልጽ ድምጽ ያሰማል",
                    "ማይክራፎን ይቀርጻል",
                    "ሁለቱም የ SIM ቦታዎች ይሰራሉ",
                    "Wi-Fi፣ ብሉቱዝ፣ GPS ይሰራሉ",
                    "Face ID ወይም የጣት አሻራ ይሰራል",
                    "የኃይል እና የድምጽ ቁልፎች ይሰራሉ",
                ]},
                {"heading": "ከመክፈልዎ በፊት", "items": [
                    "ዋጋው በድረ-ገጹ ላይ ካለው ጋር ይመሳሰላል",
                    "ከላይ ያሉትን ሁሉንም ፈትነዋል",
                    "በሁኔታው ረክተዋል",
                ]},
            ],
        },
    },

    "laptops": {
        "en": {
            "title": "💻 Before you buy this laptop",
            "subtitle": "Ask the seller to show you these things at the shop",
            "sections": [
                {"heading": "Serial number", "items": [
                    "Serial number on the box matches the laptop",
                    "Serial number matches this listing",
                ]},
                {"heading": "Battery", "items": [
                    "Ask to plug it in — does it charge to 100%?",
                    "Battery health matches what's listed",
                ]},
                {"heading": "Screen", "items": [
                    "No dead pixels or cracks",
                    "No backlight bleeding at edges",
                    "Brightness and colors normal",
                ]},
                {"heading": "Keyboard & trackpad", "items": [
                    "Every key types correctly",
                    "Trackpad responds smoothly",
                    "No sticky or missing keys",
                ]},
                {"heading": "Ports & functions", "items": [
                    "All USB ports work",
                    "HDMI and headphone jack work",
                    "Webcam and microphone work",
                    "Windows or macOS boots normally",
                ]},
                {"heading": "Before you pay", "items": [
                    "Price matches what's on the website",
                    "You've tested everything above",
                ]},
            ],
        },
        "am": {
            "title": "💻 ይህን ላፕቶፕ ከመግዛትዎ በፊት",
            "subtitle": "በሱቁ ውስጥ እነዚህን እንዲያሳይዎ ሻጩን ይጠይቁ",
            "sections": [
                {"heading": "ሲሪያል ቁጥር", "items": [
                    "በሳጥኑ ላይ ያለው ሲሪያል ቁጥር ከላፕቶፑ ጋር ይመሳሰላል",
                    "ሲሪያል ቁጥር በዚህ ዝርዝር ላይ ካለው ጋር ይመሳሰላል",
                ]},
                {"heading": "ባትሪ", "items": [
                    "እንዲሰካ ይጠይቁ — እስከ 100% ይሞላል?",
                    "የባትሪ ጤንነት ከተጠቀሰው ጋር ይመሳሰላል",
                ]},
                {"heading": "ስክሪን", "items": [
                    "የሞቱ ፒክሴሎች ወይም ስንጥቆች የሉም",
                    "በጠርዞች ላይ የብርሃን መፍሰስ የለም",
                    "ብሩህነት እና ቀለሞች በተለምዶ",
                ]},
                {"heading": "ኪቦርድ እና ትራክፓድ", "items": [
                    "ሁሉም ቁልፎች በትክክል ይጽፋሉ",
                    "ትራክፓድ በተለምዶ ምላሽ ይሰጣል",
                    "የተጣበቁ ወይም የጠፉ ቁልፎች የሉም",
                ]},
                {"heading": "ፖርቶች እና ተግባራት", "items": [
                    "ሁሉም USB ፖርቶች ይሰራሉ",
                    "HDMI እና የጆሮ ማዳመጫ ቦታ ይሰራሉ",
                    "ካሜራ እና ማይክራፎን ይሰራሉ",
                    "Windows ወይም macOS በተለምዶ ይጀምራል",
                ]},
                {"heading": "ከመክፈልዎ በፊት", "items": [
                    "ዋጋው በድረ-ገጹ ላይ ካለው ጋር ይመሳሰላል",
                    "ከላይ ያሉትን ሁሉንም ፈትነዋል",
                ]},
            ],
        },
    },

    "accessories": {
        "en": {
            "title": "🎧 Before you buy this accessory",
            "subtitle": "Quick check at the shop",
            "sections": [
                {"heading": "Packaging", "items": [
                    "Original box or packaging (if listed as new)",
                    "Serial number visible (if applicable)",
                    "Not damaged",
                ]},
                {"heading": "Functionality", "items": [
                    "Pairs with your phone or device normally",
                    "Sound or function works as expected",
                    "Battery holds charge (for wireless)",
                    "No physical damage",
                ]},
                {"heading": "Before you pay", "items": [
                    "Price matches what's on the website",
                    "You've tested it works",
                ]},
            ],
        },
        "am": {
            "title": "🎧 ይህን መለዋወጫ ከመግዛትዎ በፊት",
            "subtitle": "በሱቁ ውስጥ ፈጣን ፍተሻ",
            "sections": [
                {"heading": "ማሸጊያ", "items": [
                    "ዋናው ሳጥን ወይም ማሸጊያ (አዲስ ተብሎ ከተጠቀሰ)",
                    "ሲሪያል ቁጥር ይታያል (ካለ)",
                    "አልተጎዳም",
                ]},
                {"heading": "ተግባራት", "items": [
                    "ከስልክዎ ወይም ከመሣሪያዎ ጋር በተለምዶ ይገናኛል",
                    "ድምጽ ወይም ተግባር እንደተጠበቀው ይሰራል",
                    "ባትሪ ይይዛል (ሽቦ አልባ ለሆነ)",
                    "የአካል ጉዳት የለም",
                ]},
                {"heading": "ከመክፈልዎ በፊት", "items": [
                    "ዋጋው በድረ-ገጹ ላይ ካለው ጋር ይመሳሰላል",
                    "ይሰራ መሆኑን ፈትነዋል",
                ]},
            ],
        },
    },

    "tablets": {
        "en": {
            "title": "📟 Before you buy this tablet",
            "subtitle": "Ask the seller to show you these things at the shop",
            "sections": [
                {"heading": "Serial number", "items": [
                    "Serial number on the box matches the tablet",
                    "Serial number matches this listing",
                ]},
                {"heading": "Battery & charging", "items": [
                    "Charges normally with the included charger",
                    "Battery health as described",
                ]},
                {"heading": "Screen & functions", "items": [
                    "No dead pixels or cracks",
                    "Touch responds everywhere",
                    "Front and back cameras work",
                    "Speakers and microphone work",
                    "Wi-Fi and Bluetooth work",
                ]},
                {"heading": "Before you pay", "items": [
                    "Price matches what's on the website",
                    "You've tested everything above",
                ]},
            ],
        },
        "am": {
            "title": "📟 ይህን ታብሌት ከመግዛትዎ በፊት",
            "subtitle": "በሱቁ ውስጥ እነዚህን እንዲያሳይዎ ሻጩን ይጠይቁ",
            "sections": [
                {"heading": "ሲሪያል ቁጥር", "items": [
                    "በሳጥኑ ላይ ያለው ሲሪያል ቁጥር ከታብሌቱ ጋር ይመሳሰላል",
                    "ሲሪያል ቁጥር በዚህ ዝርዝር ላይ ካለው ጋር ይመሳሰላል",
                ]},
                {"heading": "ባትሪ እና መሙያ", "items": [
                    "ከተካተተው ቻርጀር ጋር በተለምዶ ይሞላል",
                    "የባትሪ ጤንነት እንደተገለጸው",
                ]},
                {"heading": "ስክሪን እና ተግባራት", "items": [
                    "የሞቱ ፒክሴሎች ወይም ስንጥቆች የሉም",
                    "በሁሉም ቦታ ይነካል",
                    "የፊት እና የኋላ ካሜራዎች ይሰራሉ",
                    "ስፒከሮች እና ማይክራፎን ይሰራሉ",
                    "Wi-Fi እና ብሉቱዝ ይሰራሉ",
                ]},
                {"heading": "ከመክፈልዎ በፊት", "items": [
                    "ዋጋው በድረ-ገጹ ላይ ካለው ጋር ይመሳሰላል",
                    "ከላይ ያሉትን ሁሉንም ፈትነዋል",
                ]},
            ],
        },
    },
}


def get_checklist(category_slug: str, lang: str = "en") -> dict:
    cat = CHECKLISTS.get(category_slug) or CHECKLISTS["phones"]
    return cat.get(lang) or cat.get("en") or cat


def get_safety_page(lang: str = "en") -> dict:
    checklists = {}
    for slug, langs in CHECKLISTS.items():
        checklists[slug] = langs.get(lang) or langs.get("en")
    return {
        "promise": PROMISE.get(lang) or PROMISE.get("en"),
        "checklists": checklists,
    }
def get_checklist_preview(category_slug: str, lang: str = "en") -> str:
    """Build a short, specific preview from the real checklist sections.

    e.g. for phones: "IMEI check, Battery, Screen, Functions + 1 more"
    """
    checklist = get_checklist(category_slug, lang)
    sections = checklist.get("sections", [])
    headings = [s.get("heading", "") for s in sections if s.get("heading")]
    shown = headings[:4]
    remainder = len(headings) - len(shown)
    preview = ", ".join(shown)
    if remainder > 0:
        preview += f" + {remainder} more"
=======
"""What to check before buying in person at the shop.

GEBEYA TECH is a broker service. Every item listed is available for
inspection and purchase at partner shops in Bole, Edna Mall.
"""

# =====================================================
# OUR PROMISE
# =====================================================

PROMISE = {
    "en": [
        {"icon": "✅", "title": "Real photos", "body": "The photos on the website are the actual item."},
        {"icon": "✅", "title": "Honest specs", "body": "Battery health, condition, storage — everything is written truthfully."},
        {"icon": "✅", "title": "Fair pricing", "body": "Our prices match the current Addis market. No inflated numbers."},
        {"icon": "✅", "title": "Pay at the shop, after you check", "body": "You pay the shop directly, only after you're satisfied."},
        {"icon": "✅", "title": "No deposit, no pressure", "body": "Message us to arrange viewing. Walk away if it's not right."},
    ],
    "am": [
        {"icon": "✅", "title": "እውነተኛ ፎቶዎች", "body": "በድረ-ገጹ ላይ ያሉት ፎቶዎች ትክክለኛውን ዕቃ ያሳያሉ።"},
        {"icon": "✅", "title": "ታማኝ ዝርዝር", "body": "የባትሪ ጤንነት፣ ሁኔታ፣ ማከማቻ — ሁሉም በእውነት ተጽፏል።"},
        {"icon": "✅", "title": "ተመጣጣኝ ዋጋ", "body": "ዋጋዎቻችን ከአዲስ አበባ ገበያ ጋር ይመሳሰላሉ።"},
        {"icon": "✅", "title": "በሱቁ ይክፈሉ፣ ካረጋገጡ በኋላ", "body": "ዕቃውን ካረኩ በኋላ ብቻ ለሱቁ በቀጥታ ይክፈሉ።"},
        {"icon": "✅", "title": "ቅድሚያ ክፍያ የለም", "body": "ለመመልከት ያግኙን። ዕቃው የማይስማማ ከሆነ ይራመዱ።"},
    ],
}

# =====================================================
# CATEGORY CHECKLISTS
# =====================================================

CHECKLISTS = {
    "phones": {
        "en": {
            "title": "📱 Before you buy this phone",
            "subtitle": "Ask the seller to show you these things at the shop",
            "sections": [
                {"heading": "IMEI check", "items": [
                    "Dial *#06# — the IMEI on screen matches the box",
                    "IMEI is exactly 15 digits",
                    "IMEI matches what's on this listing",
                ]},
                {"heading": "Battery", "items": [
                    "Battery health matches what's listed",
                    "Ask to plug it in — does it charge?",
                    "Feel the back — is it warm (shouldn't be)",
                ]},
                {"heading": "Screen", "items": [
                    "No cracks or dead pixels",
                    "Touch responds everywhere",
                    "Brightness adjusts normally",
                ]},
                {"heading": "Functions", "items": [
                    "Front and back cameras work",
                    "Speaker plays clear sound",
                    "Microphone records",
                    "Both SIM slots work",
                    "Wi-Fi, Bluetooth, GPS work",
                    "Face ID or fingerprint works",
                    "Power and volume buttons work",
                ]},
                {"heading": "Before you pay", "items": [
                    "Price matches what's on the website",
                    "You've tested everything above",
                    "You're satisfied with the condition",
                ]},
            ],
        },
        "am": {
            "title": "📱 ይህን ስልክ ከመግዛትዎ በፊት",
            "subtitle": "በሱቁ ውስጥ እነዚህን እንዲያሳይዎ ሻጩን ይጠይቁ",
            "sections": [
                {"heading": "IMEI ማረጋገጫ", "items": [
                    "*#06# ይደውሉ — በስክሪኑ ላይ ያለው IMEI ከሳጥኑ ጋር ይመሳሰላል",
                    "IMEI በትክክል 15 አሃዞች ነው",
                    "IMEI በዚህ ዝርዝር ላይ ካለው ጋር ይመሳሰላል",
                ]},
                {"heading": "ባትሪ", "items": [
                    "የባትሪ ጤንነት ከተጠቀሰው ጋር ይመሳሰላል",
                    "እንዲሰካ ይጠይቁ — ይሞላል?",
                    "የኋላውን ይንኩ — ሞቅ ብሎ መሆን የለበትም",
                ]},
                {"heading": "ስክሪን", "items": [
                    "ስንጥቅ ወይም የሞቱ ፒክሴሎች የሉም",
                    "በሁሉም ቦታ ይነካል",
                    "የብሩህነት መጠን በተለምዶ ይቀያየራል",
                ]},
                {"heading": "ተግባራት", "items": [
                    "የፊት እና የኋላ ካሜራዎች ይሰራሉ",
                    "ስፒከር ግልጽ ድምጽ ያሰማል",
                    "ማይክራፎን ይቀርጻል",
                    "ሁለቱም የ SIM ቦታዎች ይሰራሉ",
                    "Wi-Fi፣ ብሉቱዝ፣ GPS ይሰራሉ",
                    "Face ID ወይም የጣት አሻራ ይሰራል",
                    "የኃይል እና የድምጽ ቁልፎች ይሰራሉ",
                ]},
                {"heading": "ከመክፈልዎ በፊት", "items": [
                    "ዋጋው በድረ-ገጹ ላይ ካለው ጋር ይመሳሰላል",
                    "ከላይ ያሉትን ሁሉንም ፈትነዋል",
                    "በሁኔታው ረክተዋል",
                ]},
            ],
        },
    },

    "laptops": {
        "en": {
            "title": "💻 Before you buy this laptop",
            "subtitle": "Ask the seller to show you these things at the shop",
            "sections": [
                {"heading": "Serial number", "items": [
                    "Serial number on the box matches the laptop",
                    "Serial number matches this listing",
                ]},
                {"heading": "Battery", "items": [
                    "Ask to plug it in — does it charge to 100%?",
                    "Battery health matches what's listed",
                ]},
                {"heading": "Screen", "items": [
                    "No dead pixels or cracks",
                    "No backlight bleeding at edges",
                    "Brightness and colors normal",
                ]},
                {"heading": "Keyboard & trackpad", "items": [
                    "Every key types correctly",
                    "Trackpad responds smoothly",
                    "No sticky or missing keys",
                ]},
                {"heading": "Ports & functions", "items": [
                    "All USB ports work",
                    "HDMI and headphone jack work",
                    "Webcam and microphone work",
                    "Windows or macOS boots normally",
                ]},
                {"heading": "Before you pay", "items": [
                    "Price matches what's on the website",
                    "You've tested everything above",
                ]},
            ],
        },
        "am": {
            "title": "💻 ይህን ላፕቶፕ ከመግዛትዎ በፊት",
            "subtitle": "በሱቁ ውስጥ እነዚህን እንዲያሳይዎ ሻጩን ይጠይቁ",
            "sections": [
                {"heading": "ሲሪያል ቁጥር", "items": [
                    "በሳጥኑ ላይ ያለው ሲሪያል ቁጥር ከላፕቶፑ ጋር ይመሳሰላል",
                    "ሲሪያል ቁጥር በዚህ ዝርዝር ላይ ካለው ጋር ይመሳሰላል",
                ]},
                {"heading": "ባትሪ", "items": [
                    "እንዲሰካ ይጠይቁ — እስከ 100% ይሞላል?",
                    "የባትሪ ጤንነት ከተጠቀሰው ጋር ይመሳሰላል",
                ]},
                {"heading": "ስክሪን", "items": [
                    "የሞቱ ፒክሴሎች ወይም ስንጥቆች የሉም",
                    "በጠርዞች ላይ የብርሃን መፍሰስ የለም",
                    "ብሩህነት እና ቀለሞች በተለምዶ",
                ]},
                {"heading": "ኪቦርድ እና ትራክፓድ", "items": [
                    "ሁሉም ቁልፎች በትክክል ይጽፋሉ",
                    "ትራክፓድ በተለምዶ ምላሽ ይሰጣል",
                    "የተጣበቁ ወይም የጠፉ ቁልፎች የሉም",
                ]},
                {"heading": "ፖርቶች እና ተግባራት", "items": [
                    "ሁሉም USB ፖርቶች ይሰራሉ",
                    "HDMI እና የጆሮ ማዳመጫ ቦታ ይሰራሉ",
                    "ካሜራ እና ማይክራፎን ይሰራሉ",
                    "Windows ወይም macOS በተለምዶ ይጀምራል",
                ]},
                {"heading": "ከመክፈልዎ በፊት", "items": [
                    "ዋጋው በድረ-ገጹ ላይ ካለው ጋር ይመሳሰላል",
                    "ከላይ ያሉትን ሁሉንም ፈትነዋል",
                ]},
            ],
        },
    },

    "accessories": {
        "en": {
            "title": "🎧 Before you buy this accessory",
            "subtitle": "Quick check at the shop",
            "sections": [
                {"heading": "Packaging", "items": [
                    "Original box or packaging (if listed as new)",
                    "Serial number visible (if applicable)",
                    "Not damaged",
                ]},
                {"heading": "Functionality", "items": [
                    "Pairs with your phone or device normally",
                    "Sound or function works as expected",
                    "Battery holds charge (for wireless)",
                    "No physical damage",
                ]},
                {"heading": "Before you pay", "items": [
                    "Price matches what's on the website",
                    "You've tested it works",
                ]},
            ],
        },
        "am": {
            "title": "🎧 ይህን መለዋወጫ ከመግዛትዎ በፊት",
            "subtitle": "በሱቁ ውስጥ ፈጣን ፍተሻ",
            "sections": [
                {"heading": "ማሸጊያ", "items": [
                    "ዋናው ሳጥን ወይም ማሸጊያ (አዲስ ተብሎ ከተጠቀሰ)",
                    "ሲሪያል ቁጥር ይታያል (ካለ)",
                    "አልተጎዳም",
                ]},
                {"heading": "ተግባራት", "items": [
                    "ከስልክዎ ወይም ከመሣሪያዎ ጋር በተለምዶ ይገናኛል",
                    "ድምጽ ወይም ተግባር እንደተጠበቀው ይሰራል",
                    "ባትሪ ይይዛል (ሽቦ አልባ ለሆነ)",
                    "የአካል ጉዳት የለም",
                ]},
                {"heading": "ከመክፈልዎ በፊት", "items": [
                    "ዋጋው በድረ-ገጹ ላይ ካለው ጋር ይመሳሰላል",
                    "ይሰራ መሆኑን ፈትነዋል",
                ]},
            ],
        },
    },

    "tablets": {
        "en": {
            "title": "📟 Before you buy this tablet",
            "subtitle": "Ask the seller to show you these things at the shop",
            "sections": [
                {"heading": "Serial number", "items": [
                    "Serial number on the box matches the tablet",
                    "Serial number matches this listing",
                ]},
                {"heading": "Battery & charging", "items": [
                    "Charges normally with the included charger",
                    "Battery health as described",
                ]},
                {"heading": "Screen & functions", "items": [
                    "No dead pixels or cracks",
                    "Touch responds everywhere",
                    "Front and back cameras work",
                    "Speakers and microphone work",
                    "Wi-Fi and Bluetooth work",
                ]},
                {"heading": "Before you pay", "items": [
                    "Price matches what's on the website",
                    "You've tested everything above",
                ]},
            ],
        },
        "am": {
            "title": "📟 ይህን ታብሌት ከመግዛትዎ በፊት",
            "subtitle": "በሱቁ ውስጥ እነዚህን እንዲያሳይዎ ሻጩን ይጠይቁ",
            "sections": [
                {"heading": "ሲሪያል ቁጥር", "items": [
                    "በሳጥኑ ላይ ያለው ሲሪያል ቁጥር ከታብሌቱ ጋር ይመሳሰላል",
                    "ሲሪያል ቁጥር በዚህ ዝርዝር ላይ ካለው ጋር ይመሳሰላል",
                ]},
                {"heading": "ባትሪ እና መሙያ", "items": [
                    "ከተካተተው ቻርጀር ጋር በተለምዶ ይሞላል",
                    "የባትሪ ጤንነት እንደተገለጸው",
                ]},
                {"heading": "ስክሪን እና ተግባራት", "items": [
                    "የሞቱ ፒክሴሎች ወይም ስንጥቆች የሉም",
                    "በሁሉም ቦታ ይነካል",
                    "የፊት እና የኋላ ካሜራዎች ይሰራሉ",
                    "ስፒከሮች እና ማይክራፎን ይሰራሉ",
                    "Wi-Fi እና ብሉቱዝ ይሰራሉ",
                ]},
                {"heading": "ከመክፈልዎ በፊት", "items": [
                    "ዋጋው በድረ-ገጹ ላይ ካለው ጋር ይመሳሰላል",
                    "ከላይ ያሉትን ሁሉንም ፈትነዋል",
                ]},
            ],
        },
    },
}


def get_checklist(category_slug: str, lang: str = "en") -> dict:
    cat = CHECKLISTS.get(category_slug) or CHECKLISTS["phones"]
    return cat.get(lang) or cat.get("en") or cat


def get_safety_page(lang: str = "en") -> dict:
    checklists = {}
    for slug, langs in CHECKLISTS.items():
        checklists[slug] = langs.get(lang) or langs.get("en")
    return {
        "promise": PROMISE.get(lang) or PROMISE.get("en"),
        "checklists": checklists,
    }
def get_checklist_preview(category_slug: str, lang: str = "en") -> str:
    """Build a short, specific preview from the real checklist sections.

    e.g. for phones: "IMEI check, Battery, Screen, Functions + 1 more"
    """
    checklist = get_checklist(category_slug, lang)
    sections = checklist.get("sections", [])
    headings = [s.get("heading", "") for s in sections if s.get("heading")]
    shown = headings[:4]
    remainder = len(headings) - len(shown)
    preview = ", ".join(shown)
    if remainder > 0:
        preview += f" + {remainder} more"
>>>>>>> 8cd8cd6ae22d7b25daeee3d119f1400c35df92cb
    return preview