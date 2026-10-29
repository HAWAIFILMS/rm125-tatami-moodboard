#!/usr/bin/env bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

echo "🖼️  Step 1: Generating WebP thumbnails..."
python3 generate_thumbs.py

echo "📄 Step 2: Building editorial HTML from venues_data.json..."
python3 generate_editorial_moodboard.py

echo "📋 Step 3: Mirroring to index.html for GitHub Pages..."
cp tatami_moodboard.html index.html

echo "🚀 Step 4: Git status check..."
git status -s

if [ "$1" = "--push" ] || [ "$1" = "-p" ]; then
    MSG="${2:-feat(moodboard): update locations and media catalog}"
    echo "📦 Committing & Pushing: '$MSG'..."
    git add .
    git commit -m "$MSG"
    git push origin main
    echo "✅ Deployed live to https://hawaifilms.github.io/rm125-tatami-moodboard/"
fi
