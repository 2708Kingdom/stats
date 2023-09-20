install:
	@(\
		python3.10 -m venv venv;\
		source venv/bin/activate;\
		pip install -U pip wheel;\
		pip install -r requirements.txt;\
	)
run:
	@(\
		streamlit run Home.py;\
	)