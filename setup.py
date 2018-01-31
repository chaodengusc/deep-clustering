from setuptools import setup, find_packages

setup(name='DeWave',
      version='0.11',
      description='Single-channel blind source separation',
      long_description='Decomposing two overlapping speech signals that are \
      recoded in one channel and restoring signals for each speaker',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Build Tools',
      ],
      keywords=[
        'Blind source separation',
        'Single channel',
      ],
      url='https://github.com/chaodengusc/DeWave',
      author='Chao Deng',
      author_email='chaodengusc@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
        'tensorflow',
        'numpy',
        'scikit-learn',
        'librosa',
        'mir_eval',
      ],
      entry_points={'console_scripts':[
        'dewave-clip=DeWave.dataprep:audioclips',
        'dewave-pack=DeWave.datapack:packclips',
      ]},
      include_package_data=True,
      zip_safe=False)
