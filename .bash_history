clear
pkg update && pkg upgrade -y
pkg install python git nano -y
termux-setup-storage
mkdir GamingPlatform
cd GamingPlatform
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install flask requests colorama
GamingPlatform/
│── app.py
│── games/
│   ├── guess.py
│   └── tictactoe.py
└── requirements.txt
mkdir games
touch app.py
touch games/guess.py
touch games/tictactoe.py
touch requirements.txt
nano app.py
games/guess.py
nano games/guess.py
python app.py
nano games/tictactoe.py
