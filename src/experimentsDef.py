def getImplementationDetails():
    return {
        "baseline" : {
            "folder" : "micro-aevol2",
            "nameCuda" : "micro_aevol_gpu",
            "nameCpu" : "micro_aevol_cpu"
        },
        "openMPMutationV1" : {
            "folder" : "openMPMutationV1",
            "nameCuda" : "micro_aevol_gpu",
            "nameCpu" : "micro_aevol_cpu"
        },
        "openMPMutationV2" : {
            "folder" : "openMPMutationV2",
            "nameCuda" : "micro_aevol_gpu",
            "nameCpu" : "micro_aevol_cpu"
        },
        "CUDAV1" : {
            "folder" : "cudaV1",
            "nameCuda" : "micro_aevol_gpu",
            "nameCpu" : "micro_aevol_cpu"
        },
        "CUDAV2" : {
            "folder" : "cudaV2",
            "nameCuda" : "micro_aevol_gpu",
            "nameCpu" : "micro_aevol_cpu"
        },
        "CUDAV3" : {
            "folder" : "cudaV3",
            "nameCuda" : "micro_aevol_gpu",
            "nameCpu" : "micro_aevol_cpu"
        }
    }

def getExpDetails():
    return {
        "perDefaultCuda" : {
            "executable" : "nameCuda",
            "arg" : [
                    
            ]
        },

        "CudaWandH64" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "64",
                "-h", "64",
            ]
        },

        "perDefaultCPU" : {
            "executable" : "nameCpu",
            "arg" : [
                    
            ]
        },

        "chargeCPU" : {
            "executable" : "nameCpu",
            "arg" : [
                "-w", "128",
                "-h", "128",
                "-g", "5000",
            ]
        },

        "chargeMoreRateCPU" : {
            "executable" : "nameCpu",
            "arg" : [
                "-w", "128",
                "-h", "128",
                "-g", "5000",
                "-m", "0.001",
            ]
        },

        "chargeLessRateCPU" : {
            "executable" : "nameCpu",
            "arg" : [
                "-w", "128",
                "-h", "128",
                "-g", "5000",
                "-m", "0.000001",
            ]
        },

        "chargeGPU" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "128",
                "-h", "128",
                "-g", "5000",
            ]
        },

        "chargeMoreRateGPU" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "128",
                "-h", "128",
                "-g", "5000",
                "-m", "0.001",
            ]
        },

        "chargeFullRateGPU" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "128",
                "-h", "128",
                "-g", "5000",
                "-m", "0.01",
            ]
        },

        "chargeLessRateGPU" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "128",
                "-h", "128",
                "-g", "5000",
                "-m", "0.000001",
            ]
        },



        "GPUGraph1" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "32",
                "-h", "32",
                "-g", "500",
                "-m", "0.000001",
            ]
        },

        "GPUGraph2" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "32",
                "-h", "32",
                "-g", "500",
                "-m", "0.00001",
            ]
        },

        "GPUGraph3" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "32",
                "-h", "32",
                "-g", "500",
                "-m", "0.0001",
            ]
        },

        "GPUGraph4" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "32",
                "-h", "32",
                "-g", "500",
                "-m", "0.001",
            ]
        },

        "GPUGraph5" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "32",
                "-h", "32",
                "-g", "500",
                "-m", "0.01",
            ]
        },


        "GPUGraphV21" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "64",
                "-h", "64",
                "-g", "1000",
                "-m", "0.000001",
            ]
        },

        "GPUGraphV22" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "64",
                "-h", "64",
                "-g", "1000",
                "-m", "0.00001",
            ]
        },

        "GPUGraphV23" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "64",
                "-h", "64",
                "-g", "1000",
                "-m", "0.0001",
            ]
        },

        "GPUGraphV24" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "64",
                "-h", "64",
                "-g", "1000",
                "-m", "0.001",
            ]
        },

        "GPUGraphV25" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "64",
                "-h", "64",
                "-g", "1000",
                "-m", "0.01",
            ]
        },

}