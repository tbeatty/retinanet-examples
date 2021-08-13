from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='odtk',
    version='0.2.6',
    description='Fast and accurate single shot object detector',
    author = 'NVIDIA Corporation',
    packages=['odtk', 'odtk.backbones'],
    ext_modules=[CUDAExtension('odtk._C',
        ['csrc/extensions.cpp', 'csrc/engine.cpp', 'csrc/cuda/decode.cu', 'csrc/cuda/decode_rotate.cu', 'csrc/cuda/nms.cu', 'csrc/cuda/nms_iou.cu'],
        extra_compile_args={
            'cxx': ['-std=c++14', '-O2', '-Wall'],
            'nvcc': [
                '-std=c++14', '--expt-extended-lambda', '--use_fast_math', '-Xcompiler', '-Wall,-fno-gnu-unique'
           ],
        },
        libraries=['nvinfer', 'nvinfer_plugin', 'nvonnxparser', 'opencv_core', 'opencv_imgproc', 'opencv_highgui', 'opencv_imgcodecs'])
    ],
    cmdclass={'build_ext': BuildExtension.with_options(no_python_abi_suffix=True)},
    install_requires=[
        'torch>=1.0.0a0',
        'torchvision',
        'apex @ git+https://github.com/NVIDIA/apex',
        'pycocotools @ git+https://github.com/nvidia/cocoapi.git#subdirectory=PythonAPI',
        'pillow',
        'requests',
    ],
    entry_points = {'console_scripts': ['odtk=odtk.main:main']}
)
