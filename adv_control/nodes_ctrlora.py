import execution_context
import folder_paths

from .control_ctrlora import load_ctrlora


class CtrLoRALoader:
    @classmethod
    def INPUT_TYPES(s, context: execution_context.ExecutionContext):
        return {
            "required": {
                "base": (folder_paths.get_filename_list(context, "controlnet"), ),
                "lora": (folder_paths.get_filename_list(context, "controlnet"), ),
            },
            "hidden": {
                "context": "EXECUTION_CONTEXT",
            }
        }
    
    RETURN_TYPES = ("CONTROL_NET",)
    FUNCTION = "load_controlnet_plusplus"

    CATEGORY = "Adv-ControlNet 🛂🅐🅒🅝/CtrLoRA"

    def load_controlnet_plusplus(self, base: str, lora: str, context: execution_context.ExecutionContext):
        base_path = folder_paths.get_full_path(context, "controlnet", base)
        lora_path = folder_paths.get_full_path(context,"controlnet", lora)
        controlnet = load_ctrlora(base_path, lora_path)
        return (controlnet,)
