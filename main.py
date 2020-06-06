import requests
import json
import numpy as np
from tqdm import tqdm

slack_url = "https://slackmap.com/api/v1/spots/clusters/spots"

bbox_range = [-180,-90,180,90]
# bbox_range = [-5,50,2,58]

step_size = 4
longs = np.arange(bbox_range[0], bbox_range[2], step=step_size)
lats = np.arange(bbox_range[1], bbox_range[3], step=step_size)
total_requests = longs.shape[0] * lats.shape[0]
pbar = tqdm(total=total_requests)

lines = []
for lng in longs:
    for lat in lats:
        pbar.set_description(f"getting {lng},{lat}")
        pbar.update()
        url_w_bbox = f"{slack_url}?bbox={lng},{lat},{lng+step_size},{lat+step_size}"

        response = requests.get(url_w_bbox)
        response = response.json()

        if response:
            with open(f'data/{lng}_{lat}.json', 'w') as outfile:
                json.dump(response, outfile)

# print(lines)