/**
 * The main UI for the dashboard contains:
 * - one uploader section for Medical Record
 * - another uploader section for Guidelines
 * - continue button
 * - logic to manage state/visibility etc.
 */

"use client";

import SectionUploader from "@/components/section-uploader";
import { useDashboard } from "@/context/dashboard-context";
import { simulateDelay } from "@/utils";
import { xhrSubmitDashboard } from "../requests";
import { copytext } from "../copytext";
import { useRef, useState } from "react";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const SIM_DELAY_MILLIS = 3000;

enum DocTypes {
    medrec,
    guidelines
}

interface IUploadProps {
    onSubmitted: Function;
}

export default function UploadSection({ onSubmitted }: IUploadProps) {
    const [medResource, setMed] = useState("");
    const [guideResource, setGuide] = useState("");
    const [medText, setMedText] = useState(""); // State for medical record text input
    const [guideText, setGuideText] = useState("");
    const [isSubmitting, setSubmitting] = useState(false);
    const { setGuidelinesFile, setMedicalRecord } = useDashboard();
    const toastId = useRef<any>();
    const content = copytext.en.dashboard;

    // check if guide section should remain disabled?
    const disableGuideSection = medResource && medResource.trim().length > 0 ? false : true;

    // check if continue button should be shown
    const showContinueButton =
        medResource &&
        medResource.trim().length > 0 &&
        guideResource &&
        guideResource.trim().length > 0;

    const handleMedTextChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
            setMedText(event.target.value);
    };
    
    const handleGuideTextChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
        setGuideText(event.target.value);
    };

    // mock: simulate upload using 3s delay
    const simulateUpload = async () => {
        await simulateDelay(SIM_DELAY_MILLIS);
    };

    // update the mock upload status in the state
    const updateStatus = async (type: DocTypes, result: any) => {
        const { error } = result;
        if (error) return;

        switch (type) {
            case DocTypes.medrec:
                const urlMed = content.medrec.file;
                setMed(urlMed);
                setMedicalRecord({ url: urlMed });
                break;
            case DocTypes.guidelines:
                const urlGuide = content.guide.file;
                setGuide(urlGuide);
                setGuidelinesFile({ url: urlGuide });
                break;
        }
    };

    // show a toast
    const showToast = () => {
        toastId.current = toast(content.submitToast.pending, {
            position: "top-right",
            theme: "dark"
        });
    };

    // hide a toast
    const hideToast = () => {
        toast.dismiss(toastId.current);
    };

    // handle 'continue' button submission
    const onSubmit = async () => {
        try {
            showToast();
            setSubmitting(true);
            const payload = {
                medText: medText,
                guideText: guideText,
            };

            //await simulateDelay(800);
            const caseId = await xhrSubmitDashboard(payload);
            onSubmitted({ data: { caseId }, error: null });
            toast.success("Data stored successfully!");
        } catch (error) {
            onSubmitted({ data: null, error });
            toast.error("Failed to store data.");
        } finally {
            setSubmitting(false);
            hideToast();
        }
    };

    return (
        <>
        <div className="flex flex-row items-center w-full gap-2 upload-section-main">
            <div style={{ flex: 1 }}>
                <div className="upload-container">
                    <SectionUploader
                        task={simulateUpload}
                        onComplete={(r: any, url: string) => updateStatus(DocTypes.medrec, r)}
                        disabled={false}
                        background="#3b83f6"
                        title={content.medrec.title}
                        labels={content.medrec.labels}
                    />
                    <textarea
                        value={medText}
                        onChange={handleMedTextChange}
                        placeholder="Enter details for Medical Record"
                        className="w-full p-4 mt-2 text-lg border rounded" // Set width to full
                        rows={4} // Adjust number of rows as needed
                    />
                </div>
            </div>
            <div style={{ flex: 1 }}>
                <div className="upload-container">
                    <SectionUploader
                        task={simulateUpload}
                        onComplete={(r: any, url: string) => updateStatus(DocTypes.guidelines, r)}
                        disabled={disableGuideSection}
                        background="#f97516"
                        title={content.guide.title}
                        labels={content.guide.labels}
                    />
                    <textarea
                        value={guideText}
                        onChange={handleGuideTextChange}
                        placeholder="Enter details for Guidelines"
                        className="w-full p-4 mt-2 text-lg border rounded" // Set width to full
                        rows={4} // Adjust number of rows as needed
                        disabled={disableGuideSection}
                    />
                </div>
            </div>
        </div>
        <div className="flex flex-row justify-center w-full py-4">
            {showContinueButton && (
                <button
                    className="px-4 py-2 font-medium text-white bg-green-600 rounded"
                    disabled={isSubmitting}
                    onClick={async () => await onSubmit()}>
                    {content.button.label}
                </button>
            )}
        </div>
        <ToastContainer />
        </>
    );
}
