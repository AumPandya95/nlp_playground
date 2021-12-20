
def main(corpus):
    cat_corp = corpus.get("categorical_column_objects")
    num_corp = corpus.get("numerical_column_objects")

    for each_dict in cat_corp:
        each_dict["name"] = each_dict["name"].lower()
        each_dict.pop("singular")
        each_dict.pop("plural")
    
    for each_dict in num_corp:
        each_dict["name"] = each_dict["name"].lower()
        each_dict.pop("singular")
        each_dict.pop("plural")
    
    corpus_transformed = []
    corpus_transformed.extend(cat_corp)
    corpus_transformed.extend(num_corp)
    
    return corpus_transformed


if __name__ == "__main__":
    import json
    corp_file = open("misc/corpus.json")
    corp = json.load(corp_file)

    fin_corpus = main(corp)
    with open("misc/corpus_transformed.json", "w") as file:
        json.dump(fin_corpus, file, indent=4)
        file.close()
