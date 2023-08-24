conda create -n {{cookiecutter.directory_name}} -y
conda activate {{cookiecutter.directory_name}}
pip install -r requirements.txt
git init
uvicorn main:app --reload --proxy-headers --host 0.0.0.0 --port 80 --log-level=debug