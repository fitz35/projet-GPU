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
    }

def getExpDetails():
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
            }
        },

        # openMPMutationV2
        "openMPMutationV2" : {
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
            }
        }
    }