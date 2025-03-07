export interface Athlete {
    id: number;
    firstName: string;
    lastName: string;
    sex: "m" | "w" | "d";
    eMail: string;
    dateOfBirth: string;
    disciplines?: string[];
    feats?: Array<{
        discipline: string;
        exercise: string; 
        date: string;
        result: string;
        score: number;
    }>
}
