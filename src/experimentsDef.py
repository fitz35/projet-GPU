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

        "chargeLessRateGPU" : {
            "executable" : "nameCuda",
            "arg" : [
                "-w", "128",
                "-h", "128",
                "-g", "5000",
                "-m", "0.000001",
            ]
        }
        
}