import os

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Title
content = content.replace(
    '<title>بصمة و الابداع - Love Website</title>',
    '<title>الاء و علاء 777 - Love Website</title>'
)

# Final Message AR
finalArTarget = 'const finalMessageAR = `بصمة يا روحي ..... عايز أقولك إن من يوم ما دخلتي حياتي وكل حاجة اتغيرت للأحسن بجد، إنتي مش بس حبيبتي، إنتي سندي وضهري وكل دنيتي. اليوم اللي بدأنا فيه حكايتنا هو أسعد يوم في حياتي، وربنا يخليكي ليا ونفضل مع بعض لآخر العمر ونحقق كل اللي نفسنا فيه سوا. بحبك أوي يا أغلى حاجة في دنيتي كلها 💖🌍 .`;'
finalArRepl = 'const finalMessageAR = `بابا يا روحي عاوزه اقولك أن من اول يوم دخلت فيه حياتي وكل حاجه اتغيرت للأحسن بجد انت مش بس حبيبي انت سندي وضهري وكل ودنيتي اليوم اللي بدأنا فيه حكايتنا هوا اسعد يوم في حياتي وربنا يخليك ليا ونفضل مع بعض طول العمر ونحقق كل اللي نفسنا فيه سوا بحبك اوي يا اغلي حاجه ف دنيتي كلها🫂♥️🏠`;\n        const secondaryMessageAR = `بابا نور عيني🫂♥️حبيت أفاجئك النهارده ب المفاجأة دي بما أن النهارده نفس تاريخ اول يوم اتعرفنا فيه ويعتبر عيد حبنا 13/4/2025 اليوم اللي روحي رجعت فيه جسمي من اول وجديد التاريخ اللي قلب حياتي من جحيم ل جنه اول يوم عرفتك فيه وكانت احلا صدفه انك دخلت حياتي حبه اقولك انك كنت السند والحبيب والصاحب والاب والاهل وعوضتني عن الحنان اللي انحرمت منه سبنا بعض كتير ورجعنا تاني وبنحب بعض جدا ومش بنقدر نعيش من دون بعض حقيقي انت اكتر أنسان اسعدتني ف حياتي ورجعتني الحياه من تاني بعد ما كنت فاقده الامل صح بنتخانق كتير بس مقدرش استغني عنك بينا مسافات كتير جدا ومختلفين عن بعض جدا اول حاجه انت فلسطيني وساكن في تركيا وانا مصريه وعايشه في مصر بينا مسافات كتير بين تركيا ومصر وفيه حدود كتيره جدا بس ده مش هيمنعنا عن بعض ودي مجرد خطوط وهميه انت شخص ف قلبي وقريب مني جدا زي ما انا ف قلبك وقريبا منك جدا وطلاما احنا بنعشق بعض كل يوم وكل ليله وكل ثانيه وحبنا بيتجدد وبعد كل خناقه حبنا بيذيد وكل خناقه بتقربنا لبعض وبنعشق فيها بعض طلاما كدا يبقي المسافات دي مش هتأثر فينا يا قلبي وقريب جدا هنلتقي أن شاء الله وهنعوض المسافات دي كلها يا بابا ب اذن الله ومفيش حاجه تمنعنا عن بعض ووعد مني ليك أن هفضل اصونك وهضحي عشانك لو بروحي عشان انت شخص لطيف جدا وحبيت اهلك وانك عرفتني عليهم ومامتك لطيفه جدا🥹♥️🫂 وانت شخص لطيف وجميل ونضيف وتستاهل كل خير وعد هحارب كله عشانك وربنا يجعلنا من نصيب بعض انا لو فضلت اتكلم من هنا ل بكرا مش هخلص لأن جوا قلبي كلام كتير اوي مش مش هيكفي ف رساله ده عاوز مليون رساله ومش هخلص يا روح قلبي انت احن اب عليا بجد بعشقك وبعشق صوتك وضحكتك وبثق فيك جدا من كلل قلبي يا روحي وربنا يديم ضحكتك ويديمنا لبعض 🫂♥️`;\n        const secondaryMessageEN = `My eyes\\' light 🫂♥️ I wanted to surprise you today with this...`;\n'
content = content.replace(finalArTarget, finalArRepl)

# Game Message
target = "{lang === 'ar' ? 'كل نجمة في السما بتشهد على حبي ليكي... نورتي دنيتي يا ست البنات' : 'Every star in the sky bears witness to my love... You light up my world.'}"
repl = "{lang === 'ar' ? 'بحبك قد كل مره دعيت فيها تكون من نصيبي يا اغلي من روحي بحبك يا سيد الرجاله♥️' : 'Every star in the sky bears witness to my love... You light up my world.'}"
content = content.replace(target, repl)

# Clock AR
content = content.replace(
    'clock: { start: "الأيام اللي قضيناها (8/7/2024)"',
    'clock: { start: "الأيام اللي قضيناها (13/4/2025)"'
)

# Envelope AR
content = content.replace(
    'envelope: { mylove: "حبيبتي بصمة 💜", enter: "دخول عالمنا 💜", hint: "انقر لفتح الرسالة 💌", message: "رسالة حب ليكي..." },',
    'envelope: { mylove: "حبيبي علاء 💜", enter: "دخول عالمنا 💜", hint: "انقر لفتح الرسالة 💌", message: "رسالة حب ليك..." },'
)

# Clock EN
content = content.replace(
    'clock: { start: "The days we spent (8/7/2024)"',
    'clock: { start: "The days we spent (13/4/2025)"'
)

# Envelope EN
content = content.replace(
    'envelope: { mylove: "My Beloved Basma 💜", enter: "Enter Our World 💜", hint: "Click to open the message 💌", message: "A love message for you..." },',
    'envelope: { mylove: "My Beloved Alaa 💜", enter: "Enter Our World 💜", hint: "Click to open the message 💌", message: "A love message for you..." },'
)

# Since Clock text
content = content.replace(
    '<h3 className="text-white/60 text-[10px] md:text-base font-premium tracking-widest uppercase">Since 8 July 2024</h3>',
    '<h3 className="text-white/60 text-[10px] md:text-base font-premium tracking-widest uppercase">Since 13 April 2025</h3>'
)

# Envelope View Texts
content = content.replace(
    '<h2 className="text-4xl font-bold text-gray-800 font-sans">إلى حبيبتي بصمة 💜</h2>',
    '<h2 className="text-4xl font-bold text-gray-800 font-sans">إلى حبيبي علاء 💜</h2>'
)

# Insert secondary message in EnvelopeComponent
envTarget = "{isGrowing && <FancyText text={lang === 'ar' ? finalMessageAR : finalMessageEN} />}"
envRepl = """{isGrowing && (
                                        <>
                                            <FancyText text={lang === 'ar' ? finalMessageAR : finalMessageEN} />
                                            <div className="mt-8 pt-6 border-t border-[rgb(196,13,116)]/20 px-4 md:px-8">
                                                <p className="font-premium text-gray-600 text-lg md:text-xl leading-relaxed text-right md:text-center italic drop-shadow-[0_1px_1px_rgba(255,255,255,0.8)]" style={{ direction: 'rtl' }}>
                                                    {lang === 'ar' ? secondaryMessageAR : secondaryMessageEN}
                                                </p>
                                            </div>
                                        </>
                                    )}"""
content = content.replace(envTarget, envRepl)

# Date and Password Login
content = content.replace(
    'const firstSightDate = new Date("2024-07-08T00:00:00");',
    'const firstSightDate = new Date("2025-04-13T00:00:00");'
)
content = content.replace(
    'if (day === "1" && month === "1") {',
    'if (day === "13" && month === "1") {'
)

# Love Note messages
content = content.replace('"انتي أجمل صدفة في حياتي 💖",', '"انت أجمل صدفة في حياتي 💖",')
content = content.replace('"ضحكتك بتنور دنيتي يا بصمة ✨",', '"ضحكتك بتنور دنيتي يا علاء ✨",')
content = content.replace('"ربنا يخليكي ليا يا كل حياتي 💍",', '"ربنا يخليك ليا يا كل حياتي 💍",')

# Header Text
content = content.replace(
    '<div className="text-xl md:text-2xl font-bold font-script text-[rgb(196,13,116)]">بصمة و الابداع</div>',
    '<div className="text-xl md:text-2xl font-bold font-script text-[rgb(196,13,116)]">الاء و علاء 777</div>'
)

# Hero Text
heroTarget = '''<h1 className="text-6xl md:text-8xl font-serif font-black mb-6 leading-tight drop-shadow-[0_0_30px_rgba(255,255,255,0.3)] text-white">
                                        بصمة <span className="text-[rgb(196,13,116)] italic">&</span> الابداع
                                    </h1>'''
heroRepl = '''<h1 className="text-6xl md:text-8xl font-serif font-black mb-6 leading-tight drop-shadow-[0_0_30px_rgba(255,255,255,0.3)] text-white">
                                        الاء <span className="text-[rgb(196,13,116)] italic">&</span> علاء <span className="text-3xl md:text-5xl align-top text-[#D4AF37]">777</span>
                                    </h1>'''
content = content.replace(heroTarget, heroRepl)

# Footer Text
content = content.replace(
    '<p className="text-2xl font-script text-[rgb(196,13,116)] mb-8">إنتي كل حياتي 💖</p>',
    '<p className="text-2xl font-script text-[rgb(196,13,116)] mb-8">انت كل حياتي 💖</p>'
)

# Final Scene
finalScene1 = '''<h1 className="text-4xl xs:text-6xl md:text-9xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-pink-500 via-purple-500 to-pink-600 animate-pulse-slow mb-8 px-4">
                                    بصمة
                                </h1>'''
finalScene1Repl = '''<h1 className="text-4xl xs:text-6xl md:text-9xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-pink-500 via-purple-500 to-pink-600 animate-pulse-slow mb-8 px-4">
                                    الاء و علاء
                                </h1>'''
content = content.replace(finalScene1, finalScene1Repl)

content = content.replace(
    '<p className="mt-12 text-2xl font-script text-white/60 animate-slide-up">بصمة و بس 💖</p>',
    '<p className="mt-12 text-2xl font-script text-white/60 animate-slide-up">علاء و بس 💖</p>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Update complete.')
