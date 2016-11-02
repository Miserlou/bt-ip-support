from httptrack import HTTPTracker

TEST_IP = 'this.is.a.test'

# https://github.com/ngosang/trackerslist
urls = """http://tracker.opentrackr.org:1337/announce
http://p4p.arenabg.com:1337/announce
http://explodie.org:6969/announce
http://tracker.internetwarriors.net:1337/announce
http://tracker.mg64.net:6881/announce
http://mgtracker.org:6969/announce
http://tracker2.wasabii.com.tw:6969/announce
http://tracker1.wasabii.com.tw:6969/announce
http://tracker.baravik.org:6970/announce
http://87.248.186.252:8080/announce
http://tracker.yoshi210.com:6969/announce
http://tracker.skyts.net:6969/announce
http://open.acgtracker.com:1096/announce
http://91.218.230.81:6969/announce
http://www.wareztorrent.com/announce
http://tracker.vanitycore.co:6969/announce
http://tracker.tiny-vps.com:6969/announce
http://tracker.grepler.com:6969/announce
http://tracker.filetracker.pl:8089/announce
http://tracker.dutchtracking.nl/announce
http://retracker.krs-ix.ru/announce
http://retracker.gorcomnet.ru/announce
http://ipv4.tracker.harry.lu:80/announce
http://tracker2.itzmx.com:6961/announce
http://tracker.tordb.ml:6881/announce
http://tracker.edoardocolombo.eu:6969/announce
http://tracker.kuroy.me:5944/announce
http://0123456789nonexistent.com/announce
http://tracker.tfile.me/announce
http://torrentsmd.com:8080/announce
http://open.lolicon.eu:7777/announce
http://9.rarbg.com:2710/announce
http://announce.torrentsmd.com:6969/announce
http://bt.careland.com.cn:6969/announce
http://explodie.org:6969/announce
http://mgtracker.org:2710/announce
http://tracker.tfile.me/announce
http://tracker.torrenty.org:6969/announce
http://tracker.trackerfix.com/announce
http://www.mvgroup.org:2710/announce""".split('\n')
urls = list(set(urls))

results = {}
for announce_url in urls:

    if "udp://" in announce_url: # TODO
        continue

    print("Testing " + announce_url + "..")
    results[announce_url] = {}
    peers = None
    try:
        client = HTTPTracker(announce_url,
                info_hash='2410d4554d5ed856d69f426c38791673c59f4418',
                piece_length=1098160,
                ip=TEST_IP
        )
        peers = client.get_peers()
    except Exception as e:
        results[announce_url]['success'] = False
        results[announce_url]['message'] = e
        print("FAIL")
        print(e)
        continue

    import pdb
    pdb.set_trace()
