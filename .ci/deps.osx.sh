set -e
set -x

# Install packages with brew
brew update >/dev/null
brew outdated python3 || brew upgrade --quiet python3
python3 --version
