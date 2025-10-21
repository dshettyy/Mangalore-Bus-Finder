from flask import Flask, render_template, request

app = Flask(__name__)

# Full bus routes dictionary
ROUTES = {
    
    "1": ["State Bank", "Car Street", "Mannagudda", "Ladyhill", "Chilimbi", "Urva Stores", "Kavoor", "MCF colony", "Kunjathbail"],
    "1A": ["State Bank", "Lalbagh", "Urva Stores", "Kulur", "Thannir Bavi"],
    "1B": ["State Bank", "Car Street", "Mannagudda", "Ladyhill", "Chilimbi", "Urva Stores", "Kodikal"],
    "2": ["State Bank", "Lalbagh", "Ashoknagar", "Baikampady", "Suratkal", "Mukka"],
    "2A": ["State Bank", "Lalbagh", "Ashoknagar", "Baikampady", "Suratkal", "Mukka", "Sasihitlu"],
    "2C": ["State Bank", "Lalbagh", "Ashoknagar", "Baikampady", "Baikampady Industrial Estate", "Jokatte"],
    "2D": ["State Bank", "Lalbagh", "Ashoknagar", "Baikampady", "Baikampady Industrial Estate", "Jokatte", "Parkodi"],
    "2E": ["Kankanady", "Jyothi", "Lalbagh", "Ashoknagar", "Baikampady", "Baikampady Industrial Estate", "Jokatte", "Kalavar", "Bajpe"],
    "2F": ["Kankanady", "Jyothi", "Lalbagh", "Ashoknagar", "Baikampady", "Baikampady Industrial Estate", "Jokatte", "Kalavar", "Bajpe"],
    "3": ["State Bank", "Falnir", "Bendoorwell", "Mallikatte", "Kadri", "Bikkarnakatta", "Kulshekar", "Kudupu", "Vamanjoor", "Moodushedde"],
    "3A": ["State Bank", "Jyothi", "Bendoorwell", "Mallikatte", "Kadri", "Bikkarnakatta", "Kulshekar", "Kudupu", "Vamanjoor", "Moodushedde"],
    "3B": ["Mangaladevi", "Kankanady", "Mallikatte", "Kadri", "Bikkarnakatta", "Kulshekar", "Kudupu", "Vamanjoor", "Moodushedde"],
    "3D": ["State Bank", "Jyothi", "Bunts Hostel", "Kadri", "Vamanjoor", "Ulaibettu"],
    "4": ["State Bank", "Falnir", "Kankanady", "Bendoorwell", "Mallikatte", "Kadri", "Bikkarnakatta", "Kulshekar", "Kulshekar Chowki"],
    "4A": ["State Bank", "Falnir", "Kankanady", "Bendoorwell", "Mallikatte", "Kadri", "Nanthur", "Kulshekar", "Kaikamba", "Neermarga", "Merlapadavu"],
    "4C": ["State Bank", "Falnir", "Kankanady", "Bendoorwell", "Mallikatte", "Kadri", "Nanthur", "Kulshekar", "Kaikamba", "Neermarga"],
    "5": ["State Bank", "Jyothi", "Bendoorwell", "Kankanady", "Nandigudda", "Marnamikatta", "Morgan Gate"],
    "6A": ["State Bank", "Jyothi", "Bendoorwell", "Mallikatte", "Kadri", "Bikkarnakatta", "Kulshekar", "Shaktinagar"],
    "6B": ["State Bank", "Falnir", "Kankanady", "Bendoorwell", "Mallikatte", "Kadri", "Bikkarnakatta", "Kulshekar", "Shaktinagar"],
    "6C": ["State Bank", "Jyothi", "Bunts Hostel", "Mallikatte", "Kadri", "Bikkarnakatta", "Kulshekar", "Shaktinagar"],
    "7": ["State Bank", "Car Street", "Alake", "Mannagudda", "Ladyhill", "Chilimbi", "Urva Stores"],
    "9A": ["State Bank", "Pandeshwar", "Jeppu", "Morgan Gate", "Jeppupatna", "Ekkur", "Mugeru", "Bajal", "Bajal Pakkaladka", "J.M. Road"],
    "9B": ["State Bank", "Jyothi", "Pumpwell", "Ekkur", "Mugeru", "Bajal", "Bajal Pakkaladka", "J.M. Road"],
    "10A": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Nagori", "Padil", "Kannurbettu", "Adyar", "Adyar Launch Jetty"],
    "10B": ["State Bank", "Jyothi", "Balmatta", "Kankanady", "Pumpwell", "Nagori", "Padil", "Kannurbettu", "Adyar", "Adyar Launch Jetty"],
    "11A": ["State Bank", "Falnir", "Kankanady", "Nagori", "Garodi", "Padil", "Kannurbettu"],
    "11B": ["State Bank", "Falnir", "Kankanady", "Nagori", "Garodi", "Padil", "Jalligudde"],
    "12A": ["State Bank", "Jyothi", "Bunts Hostel", "Mallikatte", "Kadri", "Bikkarnakatta", "Kulshekar", "Kudupu", "Vamanjoor", "Gurupura", "Kaikamba", "Addoor", "Polali"],
    "12B": ["State Bank", "Jyothi", "Bunts Hostel", "Mallikatte", "Kadri", "Bikkarnakatta", "Kulshekar", "Kudupu", "Vamanjoor", "Gurupura", "Kaikamba", "Addoor", "Polali", "Kolthamajal"],
    "13": ["State Bank", "Car Street", "Mannagudda", "Ladyhill", "Chilimbi", "Urva Stores"],
    "13A": ["State Bank", "Car Street", "Mannagudda", "Ladyhill", "Chilimbi", "Urva Stores", "Kottara"],
    "13C": ["State Bank", "K.S. Rao Road", "Lalbagh", "Ladyhill", "Kuloor", "Kudremukh Housing Colony", "Hudco Colony", "Govt. Womens Polytechnic", "Govt. Quarters", "Kavoor", "Bondel"],
    "13D": ["State Bank", "K.S. Rao Road", "Lalbagh", "Ladyhill", "Kuloor", "Kudremukh Housing Colony", "Hudco Colony", "Govt. Womens Polytechnic", "Govt. Quarters", "Kavoor", "Bondel", "Padangady", "Pacchanady Beggari Colony"],
    "13E": ["Mangaladevi", "Bendoorwell", "Jyothi", "Lalbagh", "Ladyhill", "Kuloor", "Kudremukh Housing Colony", "Hudco Colony", "Govt. Womens Polytechnic", "Govt. Quarters", "Kavoor", "Bondel"],
    "14A": ["State Bank", "Jyothi", "Bendoorwell", "Mallikatte", "Kadri", "Nanthur", "Akashavani", "K.P.T", "Yeyyadi", "Konchadi", "Padangady", "Bondel"],
    "14B": ["State Bank", "Falnir", "Bendoorwell", "Mallikatte", "Kadri", "Nanthur", "Akashavani", "K.P.T", "Yeyyadi", "Konchadi", "Padangady", "Bondel"],
    "14C": ["Mangaladevi", "Morgan Gate", "Attavara", "Yemmekere", "Nandigudda", "Kankanady", "Mallikatte", "Kadri", "Nanthur", "Akashavani", "K.P.T", "Yeyyadi", "Konchadi", "Padangady", "Bondel"],
    "15": ["Mangaladevi", "Morgan Gate", "Nandigudda", "Kankanady", "Mallikatte", "Kadri Market", "Nanthur", "Akashavani", "Bejai", "KSRTC Bus Stand", "Bharat Mall", "Lalbagh", "Ladyhill", "Kuloor", "Baikampady", "Surathkal"],
    "15A": ["Mangaladevi", "Morgan Gate", "Nandigudda", "Kankanady", "Mallikatte", "Kadri Market", "Nanthur", "Akashavani", "Bejai", "KSRTC Bus Stand", "Bharat Mall", "Lalbagh", "Ladyhill", "Kuloor", "Baikampady", "Surathkal", "Krishnapur", "Katipalla"],
    "15B": ["Mangaladevi", "Morgan Gate", "Nandigudda", "Kankanady", "Mallikatte", "Kadri Market", "Nanthur", "Akashavani", "Bejai", "KSRTC Bus Stand", "Bharat Mall", "Lalbagh", "Ladyhill", "Kuloor", "Baikampady", "Surathkal", "Krishnapur", "Katipalla", "Chelairpadavu"],
    "16": ["State Bank", "Mission Street", "Azizzudin Road", "Kandathpalli", "Mandi", "Gokarnath Temple", "Kudroli", "Bokkapatna", "Boloor", "Sulthan Battery"],
    "16A": ["State Bank", "Car Street", "Alake", "Kudroli", "Bokkapatna", "Boloor", "Sulthan Battery"],
    "17": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Saibeen Complex", "Bharat Mall", "KSRTC Bus Stand", "Kapikad", "Balebail", "Kottara Cross", "Kuntikana", "Konchadi", "Mullakadu", "Kavoor", "Maravoor", "Kunjathbail"],
    "17A": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Saibeen Complex", "Bharat Mall", "KSRTC Bus Stand", "Kapikad", "Balebail", "Kottara Cross", "Kuntikana", "Konchadi", "Mullakadu", "Kavoor", "Maravoor", "Kunjathbail"],
    "17B": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Saibeen Complex", "Bharat Mall", "KSRTC Bus Stand", "Kapikad", "Balebail", "Kottara Cross", "Kuntikana", "Konchadi", "Mullakadu", "Kavoor", "Maravoor", "Kunjathbail"],
    "18": ["State Bank", "Pandeshwar", "Hoige Bazar", "Bolar", "Jeppu Market", "Morgan Gate"],
    "19": ["State Bank", "Hampankatta", "Jyothi", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Saibeen Complex", "Bharat Mall", "KSRTC Bus Stand", "Bejai", "K.P.T", "Yeyyadi", "Konchadi", "Padavinangadi", "Bondel", "Pacchanady"],
    "21": ["State Bank", "Jyothi", "Bunts Hostel", "Mallikatte", "Kadri", "Nanthur", "Bikkarnakatta", "Kulshekar", "Kaikamba", "Neermarga"],
    "22": ["State Bank", "Jyothi", "Bunts Hostel", "Mallikatte", "Nanthur", "Bikkarnakatta", "Kulshekar", "Vamanjoor", "Gurupura", "Kaikamba", "Bajpe"],
    "22A": ["State Bank", "Jyothi", "Bunts Hostel", "Mallikatte", "Nanthur", "Bikkarnakatta", "Kulshekar", "Vamanjoor", "Gurupura", "Kaikamba", "Bajpe", "Bajpe Aerodrome"],
    "23": ["State Bank", "Jyothi", "Balmatta", "Kankanady", "Pumpwell", "Nagori", "Garodi", "Padil", "Faisalnagar"],
    "27": ["State Bank", "Attavar", "Nandigudda", "Marnamikatta", "Mangaladevi"],
    "27A": ["State Bank", "Attavar", "Nandigudda", "Marnamikatta", "Mangaladevi", "Mulihitlu"],
    "29": ["State Bank", "Pandeshwar", "Yemmekere", "Bolar", "Jeppu Market", "Morgan Gate"],
    "30": ["State Bank", "Jyothi", "Balmatta", "Kankanady", "Mallikatte", "Kadri", "Nanthur", "Bikkarnakatta", "Maroli", "Padil"],
    "30A": ["State Bank", "Jyothi", "Balmatta", "Kankanady", "Mallikatte", "Kadri", "Nanthur", "Bikkarnakatta", "Maroli", "Padil", "Kannurbettu", "Adyar"],
    "30B": ["State Bank", "Jyothi", "Balmatta", "Kankanady", "Mallikatte", "Kadri", "Nanthur", "Bikkarnakatta", "Maroli", "Padil", "Kannurbettu", "Adyar", "Adyar Launch Jetty"],
    "31": ["State Bank", "PVS", "Canara College", "Empire Mall", "Ballalbagh", "Mannagudda", "Urva Market", "Shediguri"],
    "31A": ["State Bank", "K.S. Rao Road", "PVS", "Canara College", "Empire Mall", "Ballalbagh", "Lalbagh", "Ladyhill", "Urva Market", "Ashoknagar"],
    "31B": ["State Bank", "Car Street", "Mannagudda", "Urva Market", "Ashoknagar", "Dombel"],
    "33": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Saibeen Complex", "Bharat Mall", "KSRTC Bus Stand", "Kapikad", "Balebail", "Kottara Cross", "Kuntikana", "Derebail", "Konchadi", "Akashbhavan"],
    "37": ["State Bank", "Jyothi", "Balmatta", "Kankanady", "Mallikatte", "Kadri", "Nanthur", "Bikkarnakatta", "Maroli", "Padil"],
    "41A": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Ladyhill", "Kuloor", "Baikampady", "Surathkal", "Krishnapur", "Katipalla", "Chelairpadavu"],
    "42": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Kotekar", "Beeri", "Talapady"],
    "43": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Kotekar", "Beeri", "Talapady", "Kinya"],
    "44A": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Ullal", "Someshwar"],
    "44B": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Kotekar", "Eliaradavu"],
    "44C": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Ullal", "Ullal Launch Jetty"],
    "44D": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Ullal", "Kotepura"],
    "45": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Ladyhill", "Chilimbi", "Urva Store", "Kottara Chowki", "Kuloor", "Panambur", "Suratkal", "Kana", "Krishnapur", "Katipalla"],
    "45A": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Ladyhill", "Chilimbi", "Urva Store", "Kottara Chowki", "Kuloor", "Panambur", "Suratkal", "Kana", "Krishnapur", "Katipalla", "Chokkabettu"],
    "45B": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Ladyhill", "Chilimbi", "Urva Store", "Kottara Chowki", "Kuloor", "Panambur", "Suratkal", "Kana", "Krishnapur", "Katipalla", "Chokkabettu"],
    "45C": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Ladyhill", "Chilimbi", "Urva Store", "Kottara Chowki", "Kuloor", "Panambur", "Suratkal", "Kana", "Krishnapur", "Katipalla", "Mangalpete", "Kaikamba"],
    "45D": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Ladyhill", "Chilimbi", "Urva Store", "Kottara Chowki", "Kuloor", "Panambur", "Suratkal", "Kana", "Krishnapur", "Katipalla", "Mangalpete", "MRPL", "Kuthethur"],
    "45E": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Ladyhill", "Chilimbi", "Urva Store", "Kottara Chowki", "Kuloor", "Panambur", "Suratkal", "Kana", "Krishnapur", "Katipalla", "Mangalpete", "MRPL", "Kaithakurneri"],
    "45F": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Ladyhill", "Chilimbi", "Urva Store", "Kottara Chowki", "Kuloor", "Panambur", "Suratkal", "Kana", "Krishnapur", "Katipalla", "Kaikamba"],
    "45G": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Ladyhill", "Chilimbi", "Urva Store", "Kottara Chowki", "Kuloor", "Panambur", "Suratkal", "Kana", "Mason Road", "Janatha Colony"],
    "45H": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Ladyhill", "Chilimbi", "Urva Store", "Kottara Chowki", "Kuloor", "Panambur", "Suratkal", "Kana", "Krishnapur", "Katipalla", "Madhyapadavu"],
    "47": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Saibeen Complex", "Bharat Mall", "KSRTC Bus Stand", "Kapikad", "Balebail", "Kottara Cross", "Kuntikana", "Kavoor", "Maravoor", "Bajpe"],
    "47A": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Saibeen Complex", "Bharat Mall", "KSRTC Bus Stand", "Kapikad", "Balebail", "Kottara Cross", "Kuntikana", "Kavoor", "Maravoor", "Bajpe"],
    "47B": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Saibeen Complex", "Bharat Mall", "KSRTC Bus Stand", "Kapikad", "Balebail", "Kottara Cross", "Kuntikana", "Kavoor", "Maravoor", "Bajpe", "Bajpe Aerodrome"],
    "47C": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Saibeen Complex", "Bharat Mall", "KSRTC Bus Stand", "Kapikad", "Balebail", "Kottara Cross", "Kuntikana", "Kavoor", "Maravoor", "Bajpe", "Bajpe Aerodrome", "Bhatrakere", "Kattalsara"],
    "48": ["State Bank", "Jyothi", "Bunts Hostel", "Mallikatte", "Kadri", "Nanthur Cross", "KPT", "Yeyyadi", "Konchadi", "Bondel", "Kavoor", "Maravoor", "Bajpe"],
    "48A": ["State Bank", "Hampankatta", "Jyothi", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Saibeen Complex", "Bharat Mall", "KSRTC Bus Stand", "Bejai", "Bejai Church", "Yeyyadi", "Konchadi", "Bondel", "Kavoor", "Maravoor", "Bajpe"],
    "51": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Deralakatte", "Mangalore University", "Konaje"],
    "51A": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Deralakatte", "Mangalore University", "Konaje", "Inoli"],
    "53": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Ladyhill", "Chilimbi", "Urva Store", "Kottara Chowki", "Kuloor", "Panambur", "Suratkal", "Kana", "Krishnapur", "Katipalla", "Soorinje", "Tibar"],
    "53A": ["Kankanady", "Pumpwell", "Nanthur", "Kadri", "Kuloor", "Suratkal", "Chokkabettu", "Katipalla", "Soorinje", "Tibar"],
    "54": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Beeri", "Maddur", "Natekal", "Manjanady", "Thaudugoli"],
    "54A": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Deralakatte", "Natekal", "Manjanady", "Thaudugoli"],
    "55": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Kuthar", "Deralakatte", "Natekal", "Konaje", "Fajir", "Harekal", "Pavoor"],
    "55A": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Kuthar", "Deralakatte", "Natekal", "Konaje", "Fajir", "Harekala", "Pavoor", "Adyanadka"],
    "55B": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Kuthar", "Deralakatte", "Natekal", "Konaje", "Fajir", "Harekala", "Pavoor", "Munnur"],
    "56": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Deralakatte", "Mangalore University", "Konaje", "Belma", "Natekal", "Mudipu"],
    "56A": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Deralakatte", "Mangalore University", "Konaje", "Belma", "Natekal", "Mudipu", "Perande"],
    "57": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Padil", "Kannur", "Adyar", "Natekal", "Munnur", "Harekala", "Pavoor"],
    "58": ["State Bank", "Balmatta", "Jyothi", "Kankanady", "Pumpwell", "Thokkottu", "Kuthar", "Munnur", "Fajir", "Harekala", "Pavoor", "Adyanadka"],
    "59": ["State Bank", "K.S. Rao Road", "PVS", "Empire Mall", "Ballalbagh", "Lalbagh", "Ladyhill", "Chilimbi", "Urva Store", "Kottara Chowki", "Kuloor", "Panambur", "Suratkal", "Krishnapur", "Katipalla", "MRPL", "Nidige"]

}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    origin = request.form['origin'].strip().lower()
    destination = request.form['destination'].strip().lower()
    results = {}

    # Case 1: Search by bus number
    if origin.upper() in ROUTES:
        results[origin.upper()] = ROUTES[origin.upper()]
        return render_template('results.html', origin=origin.upper(), destination=None, results=results, mode='bus')

    # Case 2: Only one stop entered
    if not destination:
        for bus, route in ROUTES.items():
            route_lower = [r.lower() for r in route]
            if any(origin in stop for stop in route_lower):
                results[bus] = route
        return render_template('results.html', origin=origin.title(), destination=None, results=results, mode='one_stop')

    # Case 3: Two stops entered — check for direct routes
    for bus, route in ROUTES.items():
        route_lower = [r.lower() for r in route]

        origin_matches = [stop for stop in route_lower if origin in stop]
        dest_matches = [stop for stop in route_lower if destination in stop]

        if origin_matches and dest_matches:
            o_idx = route_lower.index(origin_matches[0])
            d_idx = route_lower.index(dest_matches[0])
            if o_idx < d_idx:
                results[bus] = route

    # ✅ If no direct buses, try connecting via "State Bank"
    if not results:
        connecting_routes = []
        for bus1, route1 in ROUTES.items():
            r1_lower = [r.lower() for r in route1]
            if any(origin in stop for stop in r1_lower) and "state bank".lower() in r1_lower:
                for bus2, route2 in ROUTES.items():
                    r2_lower = [r.lower() for r in route2]
                    if "state bank".lower() in r2_lower and any(destination in stop for stop in r2_lower):
                        connecting_routes.append({
                            "first_leg": {"bus": bus1, "route": route1},
                            "second_leg": {"bus": bus2, "route": route2}
                        })

        return render_template('results.html', origin=origin.title(), destination=destination.title(),
                               results=connecting_routes, mode='connecting')

    return render_template('results.html', origin=origin.title(), destination=destination.title(),
                           results=results, mode='route')


if __name__ == '__main__':
    app.run(debug=True)
