from src.imaging.image_validator import compare_images


def test_image_similarity():

    similarity = compare_images(
        "test_data/expected_image.png",
        "test_data/actual_image.png"
    )

    assert similarity >= 95