resource "google_compute_instance" "gpu_worker" {  
  name         = "ml-gpu-node"  
  machine_type = "n1-standard-4"  
  boot_disk { initialize_params { image = "ubuntu-2004-lts" } }  

  guest_accelerator {  
    type  = "nvidia-tesla-t4"  
    count = 1  
  }  
}  