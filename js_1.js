        function checkGPUSupport() {
            try {
                const canvas = document.createElement('canvas');
                const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
                gpuAcceleration.useONNX = !!gl;
                return !!gl;
            } catch (e) {
                gpuAcceleration.useONNX = false;
                return false;