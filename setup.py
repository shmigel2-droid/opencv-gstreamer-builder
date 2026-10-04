from setuptools import setup, find_packages

setup(
    name="opencv-python-gstreamer-custom",
    version="5.1.0.dev",  # Наша скомпільована версія OpenCV 5.x
    description="Custom Windows OpenCV 5.x build with GStreamer support",
    packages=find_packages(),
    package_data={
        "cv2": ["*.pyd"],
    },
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.19.3",  # Залежність, яку pip поставить автоматично
    ],
)
