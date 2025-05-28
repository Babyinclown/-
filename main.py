from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

heroes_by_role = {
    "мидер": ["Invoker", "Puck", "Kez", "Storm Spirit", "Ember Spirit", "Tinker", "Shadow Fiend", "Queen of Pain", "Outworld Destroyer", "Lina", "Zeus", "Viper", "Dragon Knight", "Kunkka", "Leshrac", "Templar Assassin", "Arc Warden", "Meepo", "Void Spirit", "Huskar", "Alchemist", "Magnus", "Death Prophet", "Windranger", "Sniper", "Clinkz", "Batrider", "Pugna", "Lone Druid", "Monkey King", "Necrophos", "Razor", "Tiny", "Bloodseeker", "Mirana", "Bristleback", "Dark Willow", "Primal Beast", "Pangolier", "Marci", "Hoodwink"],
    "керри": ["Anti-Mage", "Kez", "Juggernaut", "Phantom Assassin", "Luna", "Terrorblade", "Faceless Void", "Spectre", "Naga Siren", "Medusa", "Morphling", "Drow Ranger", "Arc Warden", "Troll Warlord", "Ursa", "Gyrocopter", "Monkey King", "Riki", "Slark", "Bloodseeker", "Clinkz", "Weaver", "Chaos Knight", "Sven", "Wraith King", "Lifestealer", "Phantom Lancer", "Razor", "Viper", "Dragon Knight", "Alchemist", "Bristleback", "Necrophos", "Leshrac", "Huskar", "Outworld Destroyer", "Templar Assassin", "Ember Spirit", "Void Spirit", "Storm Spirit", "Kunkka", "Lycan", "Nature's Prophet", "Broodmother", "Meepo", "Lone Druid", "Mirana", "Sniper", "Windranger", "Marci", "Hoodwink"],
    "тройка": ["Centaur Warrunner", "Timbersaw", "Legion Commander", "Tidehunter", "Underlord", "Axe", "Bristleback", "Sand King", "Slardar", "Doom", "Magnus", "Mars", "Dark Seer", "Beastmaster", "Necrophos", "Omniknight", "Dawnbreaker", "Primal Beast", "Pangolier", "Night Stalker", "Spirit Breaker", "Tusk", "Elder Titan", "Lycan", "Venomancer", "Viper", "Batrider", "Clockwerk", "Earth Spirit", "Tiny", "Undying", "Abaddon", "Brewmaster", "Chaos Knight", "Dragon Knight", "Kunkka", "Lifestealer", "Wraith King", "Huskar", "Nature's Prophet", "Enigma", "Broodmother", "Visage", "Lone Druid"],
    "семи сап": ["Earth Spirit", "Ringmaster", "Tusk", "Mirana", "Hoodwink", "Clockwerk", "Bounty Hunter", "Techies", "Pudge", "Rubick", "Snapfire", "Dark Willow", "Spirit Breaker", "Phoenix", "Marci", "Dawnbreaker", "Windranger", "Venomancer", "Nyx Assassin", "Undying", "Earthshaker", "Tiny", "Keeper of the Light", "Batrider", "Skywrath Mage", "Lina", "Leshrac", "Zeus", "Ogre Magi", "Grimstroke", "Shadow Demon", "Vengeful Spirit", "Disruptor", "Ancient Apparition", "Jakiro", "Lion", "Witch Doctor", "Crystal Maiden", "Silencer", "Oracle", "Winter Wyvern"],
    "фул сап": ["Crystal Maiden", "Ringmaster", "Lion", "Witch Doctor", "Bane", "Ogre Magi", "Shadow Shaman", "Jakiro", "Lich", "Dazzle", "Oracle", "Winter Wyvern", "Disruptor", "Silencer", "Snapfire", "Ancient Apparition", "Warlock", "Chen", "Enchantress", "Io", "Treant Protector", "Abaddon", "Omniknight", "Pugna", "Rubick", "Skywrath Mage", "Vengeful Spirit", "Phoenix", "Grimstroke", "Dark Willow", "Earth Spirit", "Keeper of the Light", "Undying", "Spirit Breaker", "Bounty Hunter", "Techies", "Tusk", "Venomancer", "Hoodwink", "Marci", "Dawnbreaker", "Mirana", "Windranger"]
}
items = [
    "Boots of Speed", "Tranquil Boots", "Arcane Boots", "Phase Boots", "Power Treads", "Guardian Greaves",
    "Vanguard", "Crimson Guard", "Pipe of Insight", "Black King Bar", "Lotus Orb", "Aeon Disk", "Shiva’s Guard", "Assault Cuirass", "Heart of Tarrasque", "Manta Style", "Linken’s Sphere", "Hurricane Pike", "Glimmer Cape", "Force Staff", "Eul’s Scepter of Divinity",
    "Mekansm", "Holy Locket", "Drum of Endurance", "Vladmir’s Offering", "Solar Crest", "Aghanim’s Scepter", "Aghanim’s Shard", "Refresher Orb", "Scythe of Vyse", "Rod of Atos", "Veil of Discord", "Spirit Vessel", "Arcane Blink", "Overwhelming Blink", "Swift Blink",
    "Daedalus", "Desolator", "Divine Rapier", "Echo Sabre", "Monkey King Bar", "Battle Fury", "Mjollnir", "Radiance", "Armlet of Mordiggian", "Shadow Blade", "Silver Edge", "Bloodthorn", "Orchid Malevolence"
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mode')
def mode():
    return render_template('mode.html')

@app.route('/role', methods=['GET', 'POST'])
def role():
    if request.method == 'POST':
        role = request.form['role']
        hero = random.choice(heroes_by_role[role])
        build = random.sample(items, 6)
        # Если был рерол, снова показать результат с той же ролью
        if request.form.get('reroll'):
            return render_template('result.html', hero=hero, build=build, request=request)
        return render_template('result.html', hero=hero, build=build, request=request)
    return render_template('role.html')

@app.route('/random', methods=['GET', 'POST'])
def full_random():
    all_heroes = sum(heroes_by_role.values(), [])
    hero = random.choice(all_heroes)
    build = random.sample(items, 6)
    if request.method == 'POST' and request.form.get('reroll'):
        return render_template('result.html', hero=hero, build=build, request=request, random_mode=True)
    return render_template('result.html', hero=hero, build=build, request=request, random_mode=True)

if __name__ == '__main__':
    app.run(debug=True)