###CUDA_PATH=/usr/local/cuda
###SDK_PATH=/usr/local/cudasdk

CUDA_PATH=/usr/common/usg/cuda/3.2/
SDK_PATH=/home/veles/NVIDIA_GPU_Computing_SDK/C
NVCC=nvcc -arch=sm_20 -I. -Xcompiler "-Wall -O3"

###CUDA_PATH=/export/opt/cuda
###SDK_PATH=/export/opt/cuda/NVIDIA_CUDA_SDK

###CUDA_PATH=/usr/local/cuda
###SDK_PATH=/usr/local/NVIDIA_CUDA_SDK

CXXFLAGS = -O3 -Wall 
###-fopenmp

all: gpu-4th gpu-6th gpu-8th

asm: gpu-4th.s gpu-6th.s gpu-8th.s

cubin: hermite4-gpu.cubin hermite6-gpu.cubin hermite8-gpu.cubin

cpu: cpu-4th cpu-6th cpu-8th

clean:
	rm -f *.o *.s *.cubin .*.swp


gpu-8th: phi-GPU.cpp hermite8-gpu.o
	mpicxx $(CXXFLAGS) -DEIGHTH -DGPU -I$(CUDA_PATH)/include -L$(CUDA_PATH)/lib64 -lcudart -o $@ $^

gpu-6th: phi-GPU.cpp hermite6-gpu.o
	mpicxx $(CXXFLAGS) -DSIXTH -DGPU -I$(CUDA_PATH)/include -L$(CUDA_PATH)/lib64 -lcudart -o $@ $^

gpu-4th: phi-GPU.cpp hermite4-gpu.o
	mpicxx $(CXXFLAGS) -DFOURTH -DGPU -I$(CUDA_PATH)/include -L$(CUDA_PATH)/lib64 -lcudart -o $@ $^


gpu-8th.s: phi-GPU.cpp
	mpicxx $(CXXFLAGS) -DEIGHTH -DGPU -I$(CUDA_PATH)/include  -S -o $@ $<

gpu-6th.s: phi-GPU.cpp
	mpicxx $(CXXFLAGS) -DSIXTH -DGPU -I$(CUDA_PATH)/include  -S -o $@ $<

gpu-4th.s: phi-GPU.cpp
	mpicxx $(CXXFLAGS) -DFOURTH -DGPU -I$(CUDA_PATH)/include  -S -o $@ $<


hermite8-gpu.o: hermite8-gpu.cu hermite8-gpu.h
	$(NVCC) -c $<

hermite6-gpu.o: hermite6-gpu.cu hermite6-gpu.h
	$(NVCC) -c $<

hermite4-gpu.o: hermite4-gpu.cu hermite4-gpu.h
	$(NVCC) -c $<


hermite8-gpu.cubin: hermite8-gpu.cu
	nvcc -I $(SDK_PATH)/common/inc -Xcompiler "-O3" -cubin $<

hermite6-gpu.cubin: hermite6-gpu.cu
	nvcc -I $(SDK_PATH)/common/inc -Xcompiler "-O3" -cubin $<

hermite4-gpu.cubin: hermite4-gpu.cu
	nvcc -I $(SDK_PATH)/common/inc -Xcompiler "-O3" -cubin $<


cpu-8th: phi-GPU.cpp hermite8.h
	mpicxx $(CXXFLAGS) -DEIGHTH  -o $@ $<

cpu-6th: phi-GPU.cpp hermite6.h
	mpicxx $(CXXFLAGS) -DSIXTH  -o $@ $<

cpu-4th: phi-GPU.cpp hermite4.h
	mpicxx $(CXXFLAGS) -DFOURTH -o $@ $<

