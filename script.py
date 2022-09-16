from googleapiclient.discovery import build
from matplotlib import pyplot as plt

plt.style.use('seaborn-darkgrid')
api_key = '#your key'
youtube = build('youtube', 'v3', developerKey=api_key)


def formatter(x, pos):
    return str(round(x / 1e6, 1))


channels = {'MrBeast': 'UCX6OQ3DkcsbYNE6H8uQQuVA', 'Markiplier': 'UC7_YxT-KID8kRbqZo7MyscQ', 'PewDiePie': 'UC-lHJZR3Gqxm24_Vd_AJ5Yw',
            'jacksepticeye': 'UCYzPXprvl5Y-Sf0g4vX-m6g', 'Vsauce': 'UC6nSFpj9HTCZ5t-N3Rm3-HA', 'Dude Perfect': 'UCRijo3ddMTht_IHyNSNXpNQ',
            'Logan Paul': 'UCG8rbF3g2AMX70yOd8vqIZg', 'Dream': 'UCTkXRDQl0luXxVQrRQvWS6w', 'penguinz0': 'UCq6VFHwMzcMXbuKyG7SQYIg',
            'H2ODelirious ': 'UCClNRixXlagwAd--5MwJKCw', 'Deji (KSI)': 'UCrqsNpKuDQZreGaxBL_a5Jg', 'The Game Theorists': 'UCo_IB5145EVNcf8hw1Kku7w',
            'Smosh': 'UCY30JRSgfhYXA6i6xX1erWg', 'Jubilee': 'UCJjSDX-jUChzOEyok9XYRJQ'}

colors = ['blue', 'red', 'firebrick', 'limegreen', 'gray', 'aqua', 'burlywood', 'lime', 'white', 'blue', 'black', 'forestgreen', 'yellow', 'yellow']
counts = {}
num = 0
for k, v in channels.items():
        request = youtube.channels().list(part='statistics', id=v)
        response = request.execute()
        video_count = int(response['items'][0]['statistics']['videoCount'])
        subscriber_count = float(response['items'][0]['statistics']['subscriberCount'])
        counts[num] = [video_count, subscriber_count, k]
        num += 1

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)

# plt.title('Popular YouTubers')
plt.xlabel('video count')
plt.ylabel('subscribers (in millions)')

for i in range(len(channels)):
        plt.scatter(counts[i][0], counts[i][1], color=colors[i])
        if counts[i][2] != 'The Game Theorists' and counts[i][2] != 'penguinz0' and counts[i][2] != 'Logan Paul':
            plt.annotate(counts[i][2], xy=(counts[i][0] + 80, counts[i][1]))
        else:
            if counts[i][2] == 'The Game Theorists':
                plt.annotate(counts[i][2], xy=(counts[i][0] + 80, counts[i][1] - 1500000))
            else:
                if counts[i][2] == 'penguinz0':
                    plt.annotate(counts[i][2], xy=(counts[i][0] + 80, counts[i][1] - 1000000))
                else:
                    plt.annotate(counts[i][2], xy=(counts[i][0] + 70, counts[i][1] - 2500000))


plt.tight_layout()
plt.xlim(0, 6100)
plt.grid(True)
plt.ylim(6_000_000, 115_000_000)
plt.show()
