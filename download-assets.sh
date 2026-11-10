#!/usr/bin/env bash
# Downloads every image, video, icon and uploaded font from the current Wix site
# into ./assets so the rebuilt site no longer depends on Wix.
# Run once from this folder:  bash download-assets.sh
set -e
cd "$(dirname "$0")"
mkdir -p _originals/album assets/video assets/icons assets/fonts

get() {  # url  dest
  if [ -s "$2" ]; then echo "skip  $2"; return; fi
  echo "get   $2"; curl -fsSL "$1" -o "$2" || echo "FAIL  $1"
}

W=https://static.wixstatic.com
# Hero video (1080p) + poster frame
get "https://video.wixstatic.com/video/fb59a6_4c9415f5cc804a90b3fba5a0b2ca89f8/1080p/mp4/file.mp4" assets/video/hero.mp4
get "$W/media/fb59a6_4c9415f5cc804a90b3fba5a0b2ca89f8f000.jpg"  assets/video/hero-poster.jpg
# Favicon, share image, social icons
get "$W/media/fb59a6_790c090860d84638baf0a48d15ee3a67~mv2.png"   assets/img/favicon.png
get "$W/media/fb59a6_a1d3889760e44a57b8addbcd8952499b~mv2.png"   assets/img/og.png
get "$W/media/11062b_b5690303a8ff470e9b1c03a24aff140b~mv2.png"   assets/icons/linkedin.png
get "$W/media/11062b_cef3b719166a4815b446d4dcfcb6120d~mv2.png"   assets/icons/instagram.png
# Fonts uploaded to the Wix site
for pair in "fb59a6_253d90d066dc4649878968d7aab25331 mingothic" \
            "fb59a6_5260a733fab149ea954bc694726337d3 maison-neue-extended-medium" \
            "fb59a6_d7207afea3b44b42a8dd91827a356f43 sf-ui-display-regular"; do
  set -- $pair
  get "$W/ufonts/$1/woff2/file.woff2" "assets/fonts/$2.woff2"
  get "$W/ufonts/$1/woff/file.woff"   "assets/fonts/$2.woff"
done
# Career Album photos (original resolution)
while read -r url dest; do [ -n "$url" ] && get "$url" "$dest"; done < assets.txt
echo "Done."
