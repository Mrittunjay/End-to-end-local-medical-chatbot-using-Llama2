# Creating a loader to load pdf data
def load_pdf_data(data_path):
    loader = DirectoryLoader(
        path=data_path,
        glob="*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True,
        use_multithreading=True
    )

    docs = loader.load()
    return docs