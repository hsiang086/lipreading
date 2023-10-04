import kaggle

kaggle.api.authenticate()
kaggle.api.dataset_download_files('ashwingupta3012/human-faces', path='./dataset', unzip=True)
