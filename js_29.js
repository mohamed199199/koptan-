                    console.error('Error sharing:', err);
                    
                    // Fallback for sharing on mobile apps
                    shareViaIntent();
                });
            } else {
                // Try fallback methods for sharing
                shareViaIntent();