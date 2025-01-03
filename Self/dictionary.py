nahin={
    "id": 101,
    "cgpa":3.42,
    "marks":{
        "phy":23,
        "che":24,
        "mat":25
    }
}
print(nahin["marks"]["che"])
print(nahin.get("marks")) #get method do not throw error, if key not found return None
print(list(nahin.items())) 
print(list(nahin.keys()))
print(list(nahin["marks"].values()))
