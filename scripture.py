#!/usr/bin/env python3

import random

# List of Bible verses
scriptures = [
    "John 3:16 - For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.",
    "Jeremiah 29:11 - For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future.",
    "Philippians 4:13 - I can do all this through him who gives me strength.",
    "Psalm 23:1 - The Lord is my shepherd, I lack nothing.",
    "Romans 8:28 - And we know that in all things God works for the good of those who love him, who have been called according to his purpose.",
    "Proverbs 3:5 - Trust in the Lord with all your heart and lean not on your own understanding.",
    "Isaiah 41:10 - So do not fear, for I am with you; do not be dismayed, for I am your God.",
    "Matthew 11:28 - Come to me, all you who are weary and burdened, and I will give you rest.",
    "Joshua 1:9 - Have I not commanded you? Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go.",
    "Ephesians 2:8 - For it is by grace you have been saved, through faith—and this is not from yourselves, it is the gift of God.",
    "Psalm 46:1 - God is our refuge and strength, an ever-present help in trouble.",
    "1 Corinthians 13:4 - Love is patient, love is kind. It does not envy, it does not boast, it is not proud.",
    "2 Timothy 1:7 - For the Spirit God gave us does not make us timid, but gives us power, love and self-discipline.",
    "Romans 12:2 - Do not conform to the pattern of this world, but be transformed by the renewing of your mind.",
    "Galatians 5:22-23 - But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control.",
    "Isaiah 40:31 - But those who hope in the Lord will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint.",
    "Matthew 6:33 - But seek first his kingdom and his righteousness, and all these things will be given to you as well.",
    "Hebrews 11:1 - Now faith is confidence in what we hope for and assurance about what we do not see.",
    "1 Peter 5:7 - Cast all your anxiety on him because he cares for you.",
    "James 1:2-3 - Consider it pure joy, my brothers and sisters, whenever you face trials of many kinds, because you know that the testing of your faith produces perseverance.",
    # Additional verses
    "Proverbs 3:6 - In all your ways submit to him, and he will make your paths straight.",
    "Romans 5:8 - But God demonstrates his own love for us in this: While we were still sinners, Christ died for us.",
    "Philippians 4:6 - Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God.",
    "Matthew 28:19 - Therefore go and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit.",
    "Ephesians 2:10 - For we are God’s handiwork, created in Christ Jesus to do good works, which God prepared in advance for us to do.",
    "Galatians 2:20 - I have been crucified with Christ and I no longer live, but Christ lives in me.",
    "Romans 12:1 - Therefore, I urge you, brothers and sisters, in view of God’s mercy, to offer your bodies as a living sacrifice, holy and pleasing to God—this is your true and proper worship.",
    "John 14:6 - Jesus answered, 'I am the way and the truth and the life. No one comes to the Father except through me.'",
    "2 Corinthians 5:17 - Therefore, if anyone is in Christ, the new creation has come: The old has gone, the new is here!",
    "Romans 10:9 - If you declare with your mouth, 'Jesus is Lord,' and believe in your heart that God raised him from the dead, you will be saved.",
    "Matthew 22:37 - Jesus replied: 'Love the Lord your God with all your heart and with all your soul and with all your mind.'",
    "Hebrews 13:5 - Keep your lives free from the love of money and be content with what you have.",
    "1 John 1:9 - If we confess our sins, he is faithful and just and will forgive us our sins and purify us from all unrighteousness.",
    "Acts 1:8 - But you will receive power when the Holy Spirit comes on you; and you will be my witnesses.",
    "James 1:12 - Blessed is the one who perseveres under trial because, having stood the test, that person will receive the crown of life.",
    "1 Peter 3:15 - But in your hearts revere Christ as Lord. Always be prepared to give an answer to everyone who asks you to give the reason for the hope that you have.",
    "2 Timothy 3:16 - All Scripture is God-breathed and is useful for teaching, rebuking, correcting and training in righteousness.",
    "1 Corinthians 10:13 - No temptation has overtaken you except what is common to mankind.",
    "Matthew 5:16 - In the same way, let your light shine before others, that they may see your good deeds and glorify your Father in heaven.",
    "Hebrews 11:6 - And without faith it is impossible to please God, because anyone who comes to him must believe that he exists.",
    "1 John 4:19 - We love because he first loved us.",
    "Psalm 19:14 - May these words of my mouth and this meditation of my heart be pleasing in your sight, Lord.",
    "John 1:1 - In the beginning was the Word, and the Word was with God, and the Word was God.",
    "Colossians 3:23 - Whatever you do, work at it with all your heart, as working for the Lord, not for human masters.",
    "Romans 6:23 - For the wages of sin is death, but the gift of God is eternal life in Christ Jesus our Lord.",
]
def get_random_scripture():
    return random.choice(scriptures)

if __name__ == "__main__":
    print(get_random_scripture())
