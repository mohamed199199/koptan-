        function handleDriveLink() {
            const link = driveLinkInput.value.trim();
            if (!link) {
                alert('الرجاء إدخال رابط صحيح');
                return;