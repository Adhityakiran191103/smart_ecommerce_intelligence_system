def test_project_package_imports():
    from src.ecommerce_intelligence import __name__ as package_name
    assert package_name == "src.ecommerce_intelligence"
