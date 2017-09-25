## Scrapes realtime data from Korean Air Quality Index site

http://www.airkorea.or.kr/

## Setup

```bash
git clone https://github.com/cochoa0x1/pykoreaqi.get

cd pykoreaqi

python setup.py install 
```

## Usage

```python
from pykoreaqi import AirKorea

aqi = AirKorea()

data = aqi.get_all_realtime()
```

note: I have no idea if the korean air quality site allows their data to be used/accessed in this manner. I assume no liability for how you use this.