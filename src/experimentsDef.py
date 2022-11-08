def getExpDetails():
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
    }


def getImplementationDetails():
    return {
            # base project
        "baseline" : {
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
                    "-g", "10000",
                ]
            }
        },

        # openMPMutationV1
        "openMPMutationV1" : {
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
            }
        }
    }