import os
import glob
import json
import re
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--course-name", required=True)
    parser.add_argument("--base-dir", default=r"D:\Relocal\lishuanglin\lineage-skill\.lineage\courses")
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = os.path.join(args.base_dir, args.course_name, "transcripts")
    os.makedirs(output_dir, exist_ok=True)

    count = 0
    for srt_file in glob.glob(os.path.join(input_dir, "*.srt")):
        basename = os.path.splitext(os.path.basename(srt_file))[0]
        
        with open(srt_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        blocks = re.split(r'\n\n+', content.strip())
        full_text = []
        segments = []
        for b in blocks:
            lines = b.split('\n')
            if len(lines) >= 3:
                time_str = lines[1]
                text = " ".join(lines[2:])
                full_text.append(text)
                segments.append({"start": 0, "end": 0, "text": text})
                
        res = {
            "full_text": "\n\n".join(full_text),
            "segments": segments,
            "video": basename,
            "duration": 600 # dummy
        }
        
        out_path = os.path.join(output_dir, f"{basename}_transcript.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
        print(f"Imported {srt_file} to {out_path}")
        count += 1
        
    print(f"\n✅ Imported {count} SRT files successfully.")

if __name__ == "__main__":
    main()
